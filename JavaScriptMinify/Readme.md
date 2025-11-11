# JS Minifier GUI – 2025 Edition

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-1f77b4?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-100%25_Working-00ff41)

> **A sleek, modern, and fully functional JavaScript minifier with a dark-themed GUI** — built for Filipino developers, by a Filipino developer.  
> **No dependencies. No bloat. Just paste, minify, save.**

---

## Screenshots

<img width="1139" height="834" alt="image" src="https://github.com/user-attachments/assets/b8fe8ec6-6848-420c-87a6-b57299a0ca01" />
*Replace with actual screenshot after first run!*

---

## Features

| Feature | Description |
|--------|-----------|
| **Paste & Minify** | Paste any JS code → instantly minified |
| **Smart Whitespace Collapse** | Removes comments, extra spaces, line breaks safely |
| **Real-time Stats** | Shows original vs minified size + % saved |
| **Copy to Clipboard** | One-click copy of minified output |
| **Save as `.min.js`** | Auto-named with date: `quicklinks-minified-20251111.min.js` |
| **Filipino UX** | Messages in Taglish for local devs |
| **Zero Dependencies** | Pure `tkinter` + `re` — works offline |
| **Dark Cyber Theme** | Easy on the eyes, Consolas font, neon accents |

---

## How to Use

### 1. Run the Script

```bash
python js_minifier_gui.py
```



## 2. Using the App

| Action       | How to Do It |
|--------------|--------------|
| **Paste JS** | Paste your code in the top box |
| **Minify**   | Click **MINIFY NOW** |
| **Copy**     | Click **Copy Output** |
| **Save**     | Click **Save .min.js** → choose location |

> **Pro Tip**: Use it to minify your **QuickLinks** dashboard script!

---

## Minification Rules

```python
- Remove // line comments
- Remove /* block comments */
- Collapse multiple whitespace → single space
- Remove spaces around operators: { } ; : , = + - * / &
- Clean common patterns: ' === ' → '==='
