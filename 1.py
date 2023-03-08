import tkinter as tk

class GUI:
    def __init__(self):
        self.create_root()

        self.root.mainloop()

    def create_root(self):
        self.width = 1200
        self.height = 700
        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.config(bg='white')
        self.root.title("Window")

GUI()