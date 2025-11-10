# js_minifier_gui.py
# FIXED VERSION - Works 100% on Windows, Python 3.12
# Developed by Arvin Acosta , Noc 11, 2025

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import re
import os
from datetime import datetime

def minify_js(code):
    # Remove comments
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    
    # Collapse whitespace safely
    code = re.sub(r'\s+', ' ', code)
    code = re.sub(r'\s?([{};:,=+\-*/&|!<>])\s?', r'\1', code)
    
    # Clean common patterns
    replacements = {
        ' === ': '===', ' !== ': '!==', ' == ': '==', ' != ': '!=',
        ' >= ': '>=', ' <= ': '<=', ' && ': '&&', ' || ': '||',
        ' => ': '=>', ' =>': '=>', '=> ': '=>'
    }
    for old, new in replacements.items():
        code = code.replace(old, new)
    
    return code.strip()

class JSMinifierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JS Minifier - 2025")
        self.root.geometry("1000x720")
        self.root.configure(bg='#0f0f0f')
        

        # Modern dark style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', padding=12, font=('Segoe UI', 10, 'bold'))
        style.configure('Title.TLabel', font=('Consolas', 18, 'bold'), foreground='#00ff41')
        style.configure('Count.TLabel', font=('Consolas', 10), foreground='#888')

        # Title
        # title = ttk.Label(root, text="JavaScript Minifier", style='Title.TLabel')
        # title.pack(pady=20)

        # Main container
        main = tk.Frame(root, bg='#0f0f0f')
        main.pack(fill='both', expand=True, padx=25, pady=10)

        # Input
        input_frame = tk.LabelFrame(main, text=" Paste Your JavaScript Here", 
                                  bg='#1e1e1e', fg='#00ff41', font=('Consolas', 12, 'bold'), padx=10, pady=10)
        input_frame.pack(fill='both', expand=True, pady=(0, 10))

        self.input_text = scrolledtext.ScrolledText(
            input_frame, wrap=tk.NONE, bg='#1e1e1e', fg='#d4d4d4',
            font=('Consolas', 11), insertbackground='white', relief='flat'
        )
        self.input_text.pack(fill='both', expand=True)

        # Buttons
        btn_frame = tk.Frame(main, bg='#0f0f0f')
        btn_frame.pack(pady=15)

        buttons = [
            ("MINIFY NOW", self.minify, '#00ff41'),
            ("Clear All", self.clear_all, '#ff4444'),
            ("Copy Output", self.copy_output, '#4488ff'),
            ("Save .min.js", self.save_file, '#ffaa00')
        ]

        for text, cmd, color in buttons:
            btn = tk.Button(btn_frame, text=text, command=cmd, bg=color, fg='white',
                          font=('Segoe UI', 10, 'bold'), relief='flat', padx=20, pady=10)
            btn.pack(side='left', padx=8)

        # Output
        output_frame = tk.LabelFrame(main, text=" Minified Result", 
                                   bg='#1e1e1e', fg='#00ff41', font=('Consolas', 12, 'bold'), padx=10, pady=10)
        output_frame.pack(fill='both', expand=True, pady=(10, 0))

        self.output_text = scrolledtext.ScrolledText(
            output_frame, wrap=tk.NONE, bg='#0a1a0a', fg='#00ff80',
            font=('Consolas', 11), relief='flat', state='disabled'
        )
        self.output_text.pack(fill='both', expand=True)

        # Status + Stats
        footer = tk.Frame(root, bg='#0f0f0f')
        footer.pack(fill='x', side='bottom')

        self.stats = tk.Label(footer, text="Ready to minify!", bg='#0f0f0f', fg='#888',
                             font=('Consolas', 10), anchor='w')
        self.stats.pack(side='left', padx=20, pady=5)

        self.status = tk.Label(footer, text="Made with love for PH Devs • 2025", 
                               bg='#1a1a1a', fg='#00ff41', font=('Segoe UI', 9), anchor='e')
        self.status.pack(side='right', padx=20, pady=5, fill='x', expand=True)

    def minify(self):
        code = self.input_text.get("1.0", tk.END).strip()
        if not code:
            messagebox.showwarning("Walang Code!", "Mag-paste muna ng JavaScript!")
            return

        try:
            minified = minify_js(code)
            self.output_text.config(state='normal')
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, minified)
            self.output_text.config(state='disabled')

            orig = len(code.encode())
            mini = len(minified.encode())
            save = 100 - (mini / orig * 100) if orig > 0 else 0

            self.stats.config(text=f"Original: {orig:,} → Minified: {mini:,} bytes | Saved: {save:.1f}%")
            self.status.config(text=f"Minified na! {datetime.now().strftime('%I:%M %p')}")

        except Exception as e:
            messagebox.showerror("Error", f"Hindi successful:\n{e}")

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')
        self.stats.config(text="Cleared!")
        self.status.config(text="Ready ulit!")

    def copy_output(self):
        result = self.output_text.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.root.update()
            self.status.config(text="Copied to clipboard!")
        else:
            messagebox.showinfo("Wala pa", "Minify muna bago kopyahin!")

    def save_file(self):
        result = self.output_text.get("1.0", tk.END).strip()
        if not result:
            messagebox.showwarning("Walang laman!", "Minify muna!")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".min.js",
            filetypes=[("Minified JS", "*.min.js"), ("JavaScript", "*.js")],
            initialfile=f"quicklinks-minified-{datetime.now().strftime('%Y%m%d')}.min.js"
        )
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(result)
                self.status.config(text=f"Naka-save: {os.path.basename(filename)}")
                messagebox.showinfo("Success!", f"Na-save na!\n{filename}")
            except Exception as e:
                messagebox.showerror("Error sa Save", str(e))

# RUN THE APP
if __name__ == "__main__":
    root = tk.Tk()
    app = JSMinifierGUI(root)
    root.mainloop()