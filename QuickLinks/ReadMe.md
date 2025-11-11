# Dynamic Personal Quick Links Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Bootstrap 5](https://img.shields.io/badge/Bootstrap%205-7952AD?logo=bootstrap&logoColor=white)

A **single-page**, **fully client-side** HTML dashboard that replaces your browser's new tab or bookmarks page with a beautiful, customizable grid of quick links. Perfect as a personal start page!

All data is stored **locally in your browser** — no server, no database, no tracking.

## 🎯 What is this?

A personalized, organized **quick links manager** that runs entirely in your browser.

- Replaces messy bookmark bars with a clean card-based grid  
- Group links by category  
- Customize name, URL, category, and icon background color  
- Works offline forever  
- Export/import your links as JSON  

## 🚀 How to Use It

### 1. Setup (30 seconds)

```bash
# 1. Copy the full HTML code from the file
# 2. Paste it into a new file called: index.html
# 3. Double-click the file or drag it into your browser
# 4. (Optional) Set it as your browser's homepage / new tab page

```
### 2. Using the Dashboard
<img width="1524" height="815" alt="image" src="https://github.com/user-attachments/assets/ef102e03-f7cf-4998-90d8-7fde4ddde2d5" />

```
ActionHow to Do ItAdd a New LinkClick + My Personal Quick Links button 
 or press Ctrl+K (Cmd+K on Mac)Open a LinkClick any shortcut card → opens in new tabEdit / DeleteClick the ⋮ menu on a card → Edit or DeleteExport DataClick the ↓ Export links as JSON button → saves quicklinks-backup.jsonImport DataClick the ↑ Import links from JSON button → select your backup file

```
## ✅ Key Features
```

Zero Server Dependency – Pure static HTML + vanilla JS
Privacy First – All data saved in IndexedDB (fallback: LocalStorage)
Smart Organization – Links auto-grouped by category
Fully Customizable – Name, URL, category, and colorful icon background
Dark Color Auto-Contrast – Dark backgrounds automatically get white icon text
Smooth Animations – Rotating rainbow border on hover ✨
Responsive Grid – Powered by Bootstrap 5 (only ~12 KB gzipped)
Keyboard Shortcut – Ctrl+K to add links instantly
Backup & Migrate – Export/import anytime

```
💻 Technical Details
```
Dependencies

Bootstrap 5 – Only grid, modal, and basic styling (CDN)
Vanilla JavaScript – No frameworks
IndexedDB – Primary storage (asynchronous, high capacity)
LocalStorage – Automatic fallback

Data Structure (each link)
json{
  "id": "abc123",
  "name": "GitHub",
  "link": "https://github.com",
  "category": "Dev",
  "color": "#238636"
}
Core Functions

openDB(), idbAdd(), idbGetAll(), idbPut(), idbDelete() → IndexedDB
lsGetAll(), lsSaveAll() → LocalStorage fallback
renderAll() → Dynamically builds entire dashboard
Smart color contrast detection for icons

Styling Highlights

CSS custom properties for easy theming
Rotating conic-gradient border animation:css@keyframes rotateBorder {
  0% { --gradient-angle: 0deg; }
  100% { --gradient-angle: 360deg; }
}

```
🎨 Customization Tips
```
Want to change the look?

Open index.html
Edit the <style> section:css:root {
  --bg: #0f0f1a;           /* Background */
  --card: #1a1a2e;         /* Card background */
  --text: #e0e0ff;         /* Text color */
  --accent: #6e56cf;       /* Buttons & accents */
}

```
📤 Export & Backup
```
Your links are saved locally, but you can backup anytime:
bashClick ↓ → quicklinks-backup.json downloaded
Move to new computer → Click ↑ → select the file
All your links restored instantly!

```
🔧 Set as Browser Start Page
```
Chrome / Edge / Brave
textSettings → On startup → Open a specific page → Add:
file:///C:/path/to/your/index.html
Firefox
textabout:preferences#home → Homepage and new windows → Custom URLs
file:///C:/path/to/your/index.html

```
🤝 Contributing
```
Feel free to fork and improve! PRs welcome for:

Dark/light theme toggle
Search bar
Drag & drop reordering
Folder support
More animations
```
📄 License
```
Free to use. Just let me know...

Created Idea by : Arvin Acosta
IT NOC - Syetem Engieer L1
ePerformax Contact Centers
