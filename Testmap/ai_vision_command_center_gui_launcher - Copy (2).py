import tkinter as tk
from tkinter import ttk

class TabColumn(tk.Frame):
    def __init__(self, parent, title, options):
        super().__init__(parent, borderwidth=1, relief="solid", padx=5, pady=5)
        
        self.title = title
        self.options = options
        self.open = False

        self.button = tk.Button(self, text=title, command=self.toggle_tab, bg="#007bff", fg="white")
        self.button.pack(fill="x", pady=(0, 5))

        # Frame voor scrollbare content
        self.tab_frame = tk.Frame(self)
        self.canvas = tk.Canvas(self.tab_frame, height=150)
        self.scrollbar = ttk.Scrollbar(self.tab_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        for opt in options:
            label = tk.Label(self.scrollable_frame, text=opt)
            label.pack(anchor="w", padx=5, pady=2)

    def toggle_tab(self):
        if self.open:
            self.tab_frame.pack_forget()
        else:
            self.tab_frame.pack(fill="both", expand=True)
            self.canvas.pack(side="left", fill="both", expand=True)
            self.scrollbar.pack(side="right", fill="y")
        self.open = not self.open

# Hoofdvenster
root = tk.Tk()
root.title("3 Kolommen Tabs")
root.geometry("800x300")

# Container met 3 kolommen
container = tk.Frame(root)
container.pack(fill="both", expand=True, padx=10, pady=10)

# Kolommen aanmaken
col1 = TabColumn(container, "Miss Batcher", ["Optie 1", "Optie 2", "Optie 3", "Optie 4", "Optie 5"])
col2 = TabColumn(container, "AI Agent Module", ["Trigger A", "Trigger B", "Trigger C", "Trigger D", "Trigger E", "Trigger F"])
col3 = TabColumn(container, "Derde Kolom", ["Keuze X", "Keuze Y", "Keuze Z"])

# Layout in 3 kolommen
col1.pack(side="left", fill="both", expand=True, padx=5)
col2.pack(side="left", fill="both", expand=True, padx=5)
col3.pack(side="left", fill="both", expand=True, padx=5)

root.mainloop()
