from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("AI Vision Command Center")
root.geometry("1280x720")  # or fullscreen if you want
root.resizable(True, True)

# Load background image
bg_image = Image.open("background.png")
bg_image = bg_image.resize((1280, 720), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = Canvas(root, width=1280, height=720)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Now draw buttons on top of canvas here

root.mainloop()
