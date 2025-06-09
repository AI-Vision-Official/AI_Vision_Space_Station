from tkinter import *
from PIL import Image, ImageTk
import os
import subprocess

# === CONFIG ===
BACKGROUND_PATH = "background_ai_vision_command_center"  # Make sure it's in the same folder
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 1920

# === CREATE GUI WINDOW ===
root = Tk()
root.title("ai_vision_command_center")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

# === LOAD BACKGROUND ===
bg_image = Image.open(BACKGROUND_PATH)
bg_image = bg_image.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# === CUSTOM FONT (if installed) ===
custom_font = ("Montserrat Alternates", 14, "bold")

# === ADD BUTTONS ===

def open_folder(path):
    if os.path.exists(path):
        os.startfile(path)
    else:
        print(f"Path not found: {path}")

def launch_google():
    subprocess.Popen(["start", "https://www.google.com"], shell=True)

# Floating button style
def create_glass_button(text, command, x, y):
    btn = Button(root, text=text, font=custom_font, bg="#000000", fg="#FFD700",  # gold text
                 activebackground="#333333", activeforeground="#FFFF99",
                 relief=FLAT, bd=0, highlightthickness=0,
                 command=command)
    canvas.create_window(x, y, window=btn)

# Example buttons
create_glass_button("Open VS Studio Code", lambda: open_folder("L:/VS_Studio_Code"), 540, 400)
create_glass_button("Open Suno Folder", lambda: open_folder("L:/suno"), 540, 460)
create_glass_button("Launch Google", launch_google, 540, 520)

# === START GUI ===
root.mainloop()
