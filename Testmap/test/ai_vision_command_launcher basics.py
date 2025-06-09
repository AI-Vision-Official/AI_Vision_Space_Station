import tkinter as tk
from PIL import Image, ImageTk

# Maak het hoofdvenster
root = tk.Tk()
root.title("Voorbeeld GUI")
root.geometry("800x600")  # Pas aan naar wens

# Laad en schaal de achtergrondafbeelding
bg_img = Image.open("jouw_afbeelding.jpg")  # Vervang door jouw bestandsnaam
bg_img = bg_img.resize((800, 600), Image.ANTIALIAS)

# Zet afbeelding om voor tkinter en houd referentie vast
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_photo)
bg_label.image = bg_photo  # ✅ Referentie vasthouden
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Voeg een tekstlabel toe bovenop de achtergrond
title_label = tk.Label(root, text="Welkom bij mijn GUI", font=("Helvetica", 24), bg="white", fg="black")
title_label.pack(pady=20)

# Voeg een knop toe
def knop_actie():
    print("Knop geklikt!")

button = tk.Button(root, text="Klik hier", command=knop_actie, font=("Helvetica", 16))
button.pack(pady=10)

# Start de GUI-lus
root.mainloop()
