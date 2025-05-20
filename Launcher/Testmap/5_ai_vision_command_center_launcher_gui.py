import os
import tkinter as tk
from tkinter import messagebox
import webbrowser

# Set up folders for your creative life — change these as needed
important_folders = {
    "Suno": "L:/Creative/SunoMusic",
    "YouTube": "L:/Creative/YouTubeProjects",
    "Inventions": "L:/Projects/Author"
}

# Create folders if they don't exist
for name, path in important_folders.items():
    os.makedirs(path, exist_ok=True)

def open_folder(path):
    if os.path.exists(path):
        os.startfile(path)
    else:
        messagebox.showerror("Error", f"Folder not found: {path}")

def launch_google():
    webbrowser.open("https://www.google.com")

def exit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("AI Visionairy Launcher")
root.configure(bg="black")
root.geometry("600x400")  # Resizable, centered

# Header
header = tk.Label(
    root,
    text="🌟 Welcome to AI Visionairy, Brigitte! 🌟",
    fg="gold",
    bg="black",
    font=("Helvetica", 18, "bold")
)
header.pack(pady=20)

# Buttons
btn_style = {
    "fg": "black",
    "bg": "gold",
    "font": ("Helvetica", 12, "bold"),
    "width": 30,
    "height": 2,
    "bd": 0
}

tk.Button(root, text="🎵 Open Suno Music Folder", command=lambda: open_folder(important_folders["Suno"]), **btn_style).pack(pady=5)
tk.Button(root, text="📹 Open YouTube Storage", command=lambda: open_folder(important_folders["YouTube"]), **btn_style).pack(pady=5)
tk.Button(root, text="🧠 Open Author Folder", command=lambda: open_folder(important_folders["Inventions"]), **btn_style).pack(pady=5)
tk.Button(root, text="🌐 Launch Google", command=launch_google, **btn_style).pack(pady=5)
tk.Button(root, text="❌ Exit", command=exit_app, **btn_style).pack(pady=20)

root.mainloop()
