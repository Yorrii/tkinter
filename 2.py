import tkinter as tk

class GUI:
    def __init__(self):
        self.create_root()
        self.create_main_frame()
        self.create_button_frame()

        self.root.mainloop()

    def create_root(self):
        self.width = 1200
        self.height = 700
        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.config(bg='white')
        self.root.title("Window")

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root, width=self.width, height=self.height, bg="powder blue")
        self.main_frame.grid_propagate(0)
        self.main_frame.pack()

    def create_button_frame(self):
        self.button_frame = tk.Frame(master=self.main_frame, background="#f2e583",
                                       width=self.width/4,
                                       height=self.height-100)
        self.button_frame.pack_propagate(0) #nastavení framu aby se nesmršťoval 
    
        self.button1 = tk.Button(self.button_frame, text="Notebook", font=('Ariel', 24), width=15, height=3, 
                            background="#737270", relief="groove", activebackground='#b3b1af')
        self.button2 = tk.Button(self.button_frame, text="Image", font=('Ariel', 24), width=15, height=3, 
                            background="#737270", relief="groove", activebackground='#b3b1af')
        self.button3 = tk.Button(self.button_frame, text="Snake game", font=('Ariel', 24), width=15, height=3, 
                            background="#737270", relief="groove", activebackground='#b3b1af')
        self.button1.pack(padx=50, pady= 35)
        self.button2.pack(padx=50, pady= 35)
        self.button3.pack(padx=50, pady= 35)

        self.button_frame.grid(padx= 25, pady= 50, column = 4, row = 0, rowspan=4)

GUI()