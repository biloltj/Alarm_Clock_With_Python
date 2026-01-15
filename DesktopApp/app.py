import webview
import os
import sys

def get_html_path():
    """
    Resolve path to index.html whether running normally
    or packaged with PyInstaller.
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'Web', 'AlarmClock.html')
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Web', 'AlarmClock.html'))

def main():
    html_path = get_html_path()

    if not os.path.exists(html_path):
        raise FileNotFoundError(f"AlarmClock.html not found at {html_path}")

    window = webview.create_window(
        title='TempoFlow – Lesson Timer',
        url=html_path,
        width=1200,
        height=800,
        resizable=True
    )

    webview.start(debug=True)

if __name__ == "__main__":
    main()
