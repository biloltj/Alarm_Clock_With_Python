# ⏱️ TempoFlow – Lesson Timer

TempoFlow is a **sequential, clock-based lesson timer** designed for structured teaching sessions such as classroom lessons, workshops, and presentations.

The application allows teachers to define lesson sections, run them sequentially with timers, receive notifications, and track total lesson duration.

---

## ✨ Features

- Sequential section timers (deterministic order)
- Global lesson timer (1 hour 30 minutes)
- Manual section start with confirmation
- Editable sections (title + duration)
- Visual completion indicators (✔ completed sections)
- Audio alerts
- Fullscreen mode
- Works offline
- Cross-platform (Web, Windows, Linux)

---

## 🧠 Core Concept

TempoFlow follows a **strict sequential execution model**:

1. Sections are defined before starting
2. Each section runs independently
3. When a section finishes:
   - The user is asked to confirm the next section
   - Completed sections remain marked
4. The global lesson timer runs continuously

---

## 📁 Project Structure

```bash
TempoFlow/
│
├── web/
│ └── index.html # Main web application (HTML/CSS/JS)
│
├── desktop/
│ └── app.py # Python desktop wrapper (PyWebView)
│
├── README.md
└── requirements.txt
```

---

## 🌐 Web Version (Primary)

### Run Locally (No Installation)

1. Open the `web/` folder
2. Double-click `index.html`
3. The app runs instantly in your browser

✔ No server  
✔ No dependencies  
✔ Works on Windows & Linux  

---

## 🖥️ Desktop Application (Python + JavaScript)

The desktop version **reuses the exact same web UI and logic**.

### Technology

- **Python**: Application launcher
- **PyWebView**: Native window rendering
- **HTML/CSS/JS**: Core application logic

This ensures:
- Zero duplication of logic
- Same behavior as web version
- Native desktop experience

---

## ▶️ Run Desktop App (Development)

### 1. Install Python (3.9+ recommended)

https://www.python.org/

### 2. Install dependencies

```bash
pip install -r requirements.txt
```
3. Run the app
```bash
python desktop/app.py
```
* 📦 Build Windows Executable (Optional)
Using PyInstaller:
```bash
pip install pyinstaller

pyinstaller --noconsole --onefile \
  --add-data "web/index.html:web" \
  desktop/app.py
```
