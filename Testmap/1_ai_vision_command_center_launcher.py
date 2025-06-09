import tkinter as tk
import os
import subprocess
import pygetwindow as gw
import time


# Create the main window
root = tk.Tk()
root.title("ai_vision_command_center")
root.geometry("400x300+{}+{}".format(DESIRED_MONITOR_X, DESIRED_MONITOR_Y))
root.attributes('-topmost', True)

# Functions for buttons
def open_vs_studio():
    try:
        # Change path to your actual VS Studio path
        subprocess.Popen([r"C:\Users\RTX2060\AppData\Local\Programs\Microsoft VS Code\Code.exe"])
    except Exception as e:
        print("Could not open VS Studio:", e)

def open_work_projects():
    os.startfile(r"L:\4. Work - Projects")

def backup_computer_data():
    print("Starting backup (mock)...")
    # We’ll replace this with real backup logic later

# Layout
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Welcome, Brigitte! 🎶💡").pack(pady=10)
tk.Button(frame, text="🎼 Launch VS Studio", command=open_vs_studio).pack(pady=5)
tk.Button(frame, text="📁 Open Work Projects Folder", command=open_work_projects).pack(pady=5)
tk.Button(frame, text="♻️ Backup Computer Data", command=backup_computer_data).pack(pady=5)

command_entry = tk.Entry(root, width=40)
command_entry.pack(pady=10)
tk.Label(root, text="(Type your command here)").pack()

# Main loop
root.mainloop()
