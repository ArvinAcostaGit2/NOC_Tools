import csv
import json
import os
from tkinter import Tk, filedialog, messagebox

def csv_to_json_converter():
    """
    Opens a file selection dialog to choose a CSV file, converts its 
    contents to JSON format, and saves the JSON output.
    """
    
    # 1. Hide the main Tk window and open the file dialog
    root = Tk()
    root.withdraw() # Hides the main window
    
    messagebox.showinfo("Select CSV File", "Please select the CSV file you wish to convert.")

    # Open file dialog, filtering for CSV files
    csv_filepath = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )

    if not csv_filepath:
        messagebox.showwarning("Cancelled", "File selection cancelled. Exiting.")
        return

    # Check if the selected file actually exists and is a CSV
    if not os.path.exists(csv_filepath) or not csv_filepath.lower().endswith('.csv'):
        messagebox.showerror("Error", "Invalid file selected. Please choose a valid CSV file.")
        return
        
    data = []
    
    try:
        # 2. Read the CSV file
        # 'r' mode for reading, 'utf-8' encoding for general compatibility
        with open(csv_filepath, 'r', encoding='utf-8') as file:
            # DictReader uses the first row as dictionary keys (headers)
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        
        # 3. Determine output path
        # Get the directory and base filename (without extension)
        base_dir = os.path.dirname(csv_filepath)
        base_filename = os.path.splitext(os.path.basename(csv_filepath))[0]
        json_filepath = os.path.join(base_dir, f"{base_filename}.json")

        # 4. Write the JSON file
        # 'w' mode for writing, using indent=4 for clean, human-readable formatting
        with open(json_filepath, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        # 5. Success message
        messagebox.showinfo("Success 🎉", f"Conversion successful!\nJSON file saved to:\n{json_filepath}")

    except FileNotFoundError:
        messagebox.showerror("Error", "The specified file was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during conversion:\n{e}")

if __name__ == '__main__':
    csv_to_json_converter()