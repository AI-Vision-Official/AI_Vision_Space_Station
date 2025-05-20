# File: ai_vision_command_center_gui.py
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

# Main app class
class AIVisionairyApp:
    def __init__(self, root):
        root.title("🌟 AI Vision Command Center 🌟")
        root.configure(bg="#000000")  # Black background
        root.geometry("800x600")
        root.minsize(600, 400)

        self.header = tk.Label(root, text="AI Vision Command Center", font=("Segoe UI", 24, "bold"), fg="#FFD700", bg="#000000")
        self.header.pack(pady=20)

        self.buttons_frame = tk.Frame(root, bg="#000000")
        self.buttons_frame.pack(pady=10)

        buttons = [
            ("🌐 Heal the World Project Folder", lambda: self.open_folder(""L:\4. Work - Projects\Project - Heal The World Project")),
            ("🎵 Suno Music Folder", lambda: self.open_folder("L:\4. Work - Projects\Project - Suno")),
            ("📁 YouTube Storage", lambda: self.open_folder("L:\4. Work - Projects")),
            ("💡 Author Folder", lambda: self.open_folder(""L:\2. Personal\@Publicaties")),
            ("🌐 Launch Google", lambda: webbrowser.open("https://www.google.com")),
            ("🚀 Fullscreen Toggle", self.toggle_fullscreen),
            ("❌ Exit", root.quit)
        ]

        for text, command in buttons:
            b = tk.Button(self.buttons_frame, text=text, font=("Segoe UI", 14),
                          fg="#FFD700", bg="#1c1c1c", activebackground="#333333", activeforeground="#ffffff",
                          relief="flat", padx=10, pady=10, command=command)
            b.pack(pady=5, fill="x", expand=True)

        self.fullscreen = False
        root.bind("<F11>", lambda e: self.toggle_fullscreen())
        root.bind("<Escape>", lambda e: self.exit_fullscreen())

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        root.attributes("-fullscreen", self.fullscreen)

    def exit_fullscreen(self):
        self.fullscreen = False
        root.attributes("-fullscreen", False)

    def open_folder(self, path):
        if os.path.exists(path):
            os.startfile(path)
        else:
            messagebox.showerror("Error", f"Folder not found:\n{path}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = AIVisionairyApp(root)
    root.mainloop()
