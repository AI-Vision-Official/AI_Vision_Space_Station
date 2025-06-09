import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageTk

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("AI Vision Command Center")
root.geometry("1280x720")  # Adjust to your screen resolution
root.resizable(True, True)

# ---------- BACKGROUND ----------
bg_path = "Background_ai_vision_command_center.png"
bg_img = Image.open(bg_path).resize((1280, 720), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---------- SONG CREATOR ----------
def open_song_creator():
    song_win = tk.Toplevel(root)
    song_win.title("Create New Song")
    song_win.geometry("700x720")
    song_win.configure(bg="black")

    # Entry Fields
    tk.Label(song_win, text="Title:", fg="yellow", bg="black").pack()
    title_entry = tk.Entry(song_win, width=60)
    title_entry.pack()

    tk.Label(song_win, text="Artist/Alias:", fg="yellow", bg="black").pack()
    artist_entry = tk.Entry(song_win, width=60)
    artist_entry.pack()

    tk.Label(song_win, text="Tags (comma-separated):", fg="yellow", bg="black").pack()
    tags_entry = tk.Entry(song_win, width=60)
    tags_entry.pack()

    # ---------- Prompt Builder ----------
    tk.Label(song_win, text="Mood:", fg="yellow", bg="black").pack()
    mood_var = tk.StringVar(song_win)
    mood_var.set("Inspiring")
    tk.OptionMenu(song_win, mood_var, "Inspiring", "Sad", "Happy", "Dark", "Romantic", "Aggressive").pack()

    tk.Label(song_win, text="Voice Type:", fg="yellow", bg="black").pack()
    voice_var = tk.StringVar(song_win)
    voice_var.set("Male")
    tk.OptionMenu(song_win, voice_var, "Male", "Female", "Duet", "Robotic", "Child", "Old Voice").pack()

    tk.Label(song_win, text="Style:", fg="yellow", bg="black").pack()
    style_var = tk.StringVar(song_win)
    style_var.set("Pop")
    tk.OptionMenu(song_win, style_var, "Pop", "Rock", "Cinematic", "EDM", "Trap", "Classical").pack()

    # ---------- Idea Box ----------
    tk.Label(song_win, text="Your Song Idea / Theme:", fg="yellow", bg="black").pack()
    idea_box = tk.Entry(song_win, width=60)
    idea_box.pack()

    # ---------- Recap Label ----------
    recap_label = tk.Label(song_win, text="", fg="lightgreen", bg="black", wraplength=600, justify="left")
    recap_label.pack(pady=10)

    # ---------- Generate Prompt ----------
    def generate_prompt():
        mood = mood_var.get()
        voice = voice_var.get()
        style = style_var.get()
        idea = idea_box.get()
        title = title_entry.get().strip()

        prompt = (
            f"Create a song with the title '{title}' in a {mood.lower()} mood, "
            f"with a {voice.lower()} voice, in a {style.lower()} style.\n"
            f"Main theme: {idea}"
        )

        # Update recap label instead of messagebox
        recap_label.config(text=prompt)

    tk.Button(song_win, text="Generate Prompt", command=generate_prompt, bg="#333", fg="white").pack(pady=5)

    # ---------- Lyrics Text Area ----------
    tk.Label(song_win, text="Lyrics:", fg="yellow", bg="black").pack()
    lyrics_text = tk.Text(song_win, width=80, height=10, wrap=tk.WORD)
    lyrics_text.pack(pady=10)

    def save_song():
        title = title_entry.get().strip()
        artist = artist_entry.get().strip()
        tags = tags_entry.get().strip()
        lyrics = lyrics_text.get("1.0", tk.END).strip()

        if not title or not lyrics:
            messagebox.showwarning("Missing Info", "Please provide both title and lyrics.")
            return

        song_folder = os.path.join("Songs", title)
        os.makedirs(song_folder, exist_ok=True)

        lyrics_path = os.path.join(song_folder, f"{title}.txt")
        with open(lyrics_path, "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\nArtist: {artist}\nTags: {tags}\n\nLyrics:\n{lyrics}")

        for ext in [".mp3", ".wav", ".mp4"]:
            open(os.path.join(song_folder, title + ext), 'a').close()

        messagebox.showinfo("Saved!", f"Song '{title}' saved successfully!")
        song_win.destroy()

    tk.Button(song_win, text="Save Song", command=save_song, bg="green", fg="white").pack(pady=10)


# ---------- PUZZLE CREATOR ----------
def open_puzzle_creator():
    win = tk.Toplevel(root)
    win.title("Puzzle Creator")
    win.geometry("600x650")
    win.configure(bg="white")

    words_entry, grid_size_var, twist_var, secret_entry, preview_box = create_puzzle_inputs(win)

    def generate_puzzle():
        words, size, grid = initialize_puzzle(words_entry, grid_size_var)
        grid = place_words(grid, words, twist_var.get())
        fill_empty_spots(grid)
        display_puzzle(grid, preview_box)
        store_puzzle_data(win, grid, words, secret_entry)

    def export_puzzle():
        export_puzzle_as_image(win)

    create_puzzle_buttons(win, generate_puzzle, export_puzzle)


def create_puzzle_inputs(win):
    tk.Label(win, text="Words (comma separated):", bg="white").pack()
    words_entry = tk.Entry(win, width=60)
    words_entry.pack()

    tk.Label(win, text="Grid Size:", bg="white").pack()
    grid_size_var = tk.IntVar(value=15)
    tk.OptionMenu(win, grid_size_var, *range(10, 21)).pack()

    twist_var = tk.BooleanVar()
    tk.Checkbutton(win, text="Allow Diagonals / Reverse", variable=twist_var, bg="white").pack()

    tk.Label(win, text="Hidden Quote / Link (optional):", bg="white").pack()
    secret_entry = tk.Entry(win, width=60)
    secret_entry.pack()

    preview_box = tk.Text(win, width=50, height=15, font=("Courier", 10))
    preview_box.pack(pady=10)

    return words_entry, grid_size_var, twist_var, secret_entry, preview_box


def initialize_puzzle(words_entry, grid_size_var):
    words = [w.strip().upper() for w in words_entry.get().split(',') if w.strip()]
    size = grid_size_var.get()
    grid = [['' for _ in range(size)] for _ in range(size)]
    return words, size, grid


def place_words(grid, words, allow_diagonal):
    directions = ['H', 'V']
    if allow_diagonal:
        directions += ['D1', 'D2', 'REV']

    size = len(grid)
    for word in words:
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            direction, x, y, dx, dy = get_random_placement(size, directions, word)
            fits = check_word_fits(grid, word, x, y, dx, dy)
            if fits:
                place_word_in_grid(grid, word, x, y, dx, dy)
                placed = True
            attempts += 1
    return grid


def get_random_placement(size, directions, word):
    direction = random.choice(directions)
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    dx, dy = get_direction_offsets(direction, word)
    return direction, x, y, dx, dy


def get_direction_offsets(direction, word):
    if direction == 'H':
        return 1, 0
    elif direction == 'V':
        return 0, 1
    elif direction == 'D1':
        return 1, 1
    elif direction == 'D2':
        return -1, 1
    elif direction == 'REV':
        word = word[::-1]
        return 1, 0
    return 0, 0


def check_word_fits(grid, word, x, y, dx, dy):
    size = len(grid)
    for i in range(len(word)):
        nx, ny = x + dx * i, y + dy * i
        if not (0 <= nx < size and 0 <= ny < size) or grid[ny][nx] not in ('', word[i]):
            return False
    return True


def place_word_in_grid(grid, word, x, y, dx, dy):
    for i in range(len(word)):
        nx, ny = x + dx * i, y + dy * i
        grid[ny][nx] = word[i]


def fill_empty_spots(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '':
                grid[y][x] = random.choice(string.ascii_uppercase)


def display_puzzle(grid, preview_box):
    puzzle_text = '\n'.join([' '.join(row) for row in grid])
    preview_box.delete(1.0, tk.END)
    preview_box.insert(tk.END, puzzle_text)


def store_puzzle_data(win, grid, words, secret_entry):
    win.generated_grid = grid
    win.words_used = words
    win.secret = secret_entry.get()


def export_puzzle_as_image(win):
    if not hasattr(win, 'generated_grid'):
        return

    grid = win.generated_grid
    cell_size = 30
    img_size = len(grid) * cell_size
    img = Image.new("RGB", (img_size, img_size + 50), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            draw.text((x * cell_size + 8, y * cell_size + 5), char, fill="black", font=font)

    draw.text((10, img_size + 10), f"Hidden: {win.secret}", fill="gray", font=font)

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    if save_path:
        img.save(save_path)


def create_puzzle_buttons(win, generate_puzzle, export_puzzle):
    tk.Button(win, text="Generate Puzzle", command=generate_puzzle, bg="lightblue").pack(pady=5)
    tk.Button(win, text="Export as PNG", command=export_puzzle, bg="lightgreen").pack(pady=5)

# === Backup Function ===
def backup_script():
    try:
        src = "ai_vision_command_center_launcher_gui.py"
        dst = "ai_vision_command_center_launcher_gui_backup.py"
        shutil.copy(src, dst)
        messagebox.showinfo("Backup", "Backup saved as:\n" + dst)
    except Exception as e:
        messagebox.showerror("Backup Failed", str(e))

# Define the buttons (Text, Path, X, Y)
buttons = [
    ("ChatGPT", r"C:\Users\RTX2060\AppData\Local\Programs\Python\Python313\python.exe", 540, 200),
    ("VS Studio Code", r"C:\Users\RTX2060\AppData\Local\Programs\Microsoft VS Code\Code.exe", 540, 260),
    ("Google Chat", r"https://chat.google.com/", 540, 320),
    ("Photopea", r"https://www.photopea.com", 540, 380),
    ("Pixabay", r"https://pixabay.com", 540, 440),
    ("YouTube", r"https://www.youtube.com", 540, 500),
    ("Exit", "exit", 540, 560)
]

# ---------- Define Buttons ----------
buttons = [
    ("AI Agents", r"F:\DreamFactory\AI Agents", 540, 80),
    ("Suno", r"F:\DreamFactory\Suno", 540, 120),
    ("Projects", r"F:\DreamFactory\Projects", 540, 160),
    ("Music Files", r"F:\DreamFactory\Music Files", 540, 200),
    ("ChatGPT", r"https://chat.google.com/", 540, 240),
    ("FL Studio", r"C:\Program Files\Image-Line\FL Studio 2024\\FL64.exe", 540, 280),
    ("Google Chat", r"https://mail.google.com/chat/u/0/#chat/home/welcome", 540, 320),
    ("Photopea", r"https://www.photopea.com", 540, 360),
    ("Pixabay", r"https://pixabay.com", 540, 400),
    ("YouTube", r"https://www.youtube.com", 540, 440),
    ("APP Creator", "generate_app", 540, 480),
    ("Puzzle Creator", "generate_puzzle", 540, 520),
    ("Create Song", "create_song", 540, 560),
    ("Quick Backup", backup_script, 540, 600),
    ("Exit", "exit", 540, 640)
]

# ---------- Create and Place Buttons ----------
for text, path, x, y in buttons:
    def open_path(p=path):
        if p == "exit":
            root.destroy()
        elif p == "create_song":
            open_song_creator()
        elif p == "generate_puzzle":
            open_puzzle_creator()
        elif p.startswith("https"):
            os.system(f'start {p}')
        else:
            os.startfile(p)

    btn = tk.Button(
        root,
        text=text,
        command=open_path,
        font=('Montserrat Alternates', 14, 'bold'),
        bg="#000000",
        fg="yellow",
        width=15,
        height=0
    )
    btn.place(x=x, y=y)

root.mainloop()


