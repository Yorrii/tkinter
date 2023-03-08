import tkinter as tk
from tkinter import colorchooser

class GUI:
    def __init__(self):
        self.create_root()
        self.create_main_frame()
        self.create_button_frame()
        self.create_change_frame()
        self.create_menu()

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
                            background="#737270", relief="groove", activebackground='#b3b1af', command=self.Notebook)
        self.button2 = tk.Button(self.button_frame, text="Image", font=('Ariel', 24), width=15, height=3, 
                            background="#737270", relief="groove", activebackground='#b3b1af')
        self.button3 = tk.Button(self.button_frame, text="Snake game", font=('Ariel', 24), width=15, height=3, 
                            background="#737270", relief="groove", activebackground='#b3b1af')
        self.button1.pack(padx=50, pady= 35)
        self.button2.pack(padx=50, pady= 35)
        self.button3.pack(padx=50, pady= 35)

        self.button_frame.grid(padx= 25, pady= 50, column = 4, row = 0, rowspan=4)

    def create_change_frame(self):
        self.left_side_frame = tk.Frame(self.main_frame, width=3*self.width/4-100,
                                 height=self.height-100, bg="powder blue")
        self.left_side_frame.pack_propagate(0)
        

        self.change_frame = tk.Frame(self.left_side_frame, width=3*self.width/4-100,
                                 height=self.height-300, bg="black")
                
        self.bottom_left_frame = tk.Frame(self.left_side_frame, width=3*self.width/4-100,
                                          height= self.height-500,bg= "yellow")

        self.Notebook()
        self.change_frame.pack(fill="both", expand=1)
        self.bottom_left_frame.pack(fill='both', expand=1)      
        self.left_side_frame.grid(padx= 25, pady= 50, row= 0, column= 0, rowspan=3, columnspan=3)

    def create_menu(self):
        self.menu = tk.Menu(self.root, tearoff=1)
        
        self.file_manu = tk.Menu(self.menu, tearoff=0)
        self.option = tk.Menu(self.menu, tearoff=0)

        save_button = tk.Button(self.file_manu)
        self.file_manu.add_cascade(label="Save", menu=save_button)

        self.color_menu = tk.Menu(self.option, tearoff=0)
        change_color_button = tk.Button(self.color_menu)
        
        self.color_menu.add_cascade(label="Outer Window", menu=change_color_button, command= self.change_color_main)
        self.color_menu.add_cascade(label="Button Frame", menu=change_color_button, command= self.change_color_btnframe)
        self.color_menu.add_cascade(label="Buttons", menu=change_color_button, command= self.change_color_button)

        self.option.add_cascade(label="Change color", menu= self.color_menu)
        
        self.menu.add_cascade(label="File", menu=self.file_manu)
        self.menu.add_cascade(label="Options", menu=self.option)
        self.root.config(menu=self.menu)

    def Notebook(self):
        self.change_window_destroyer()
        for childen in self.button_frame.winfo_children():
            childen['state'] = "normal" 
        self.button1['state'] = "disable"      
        self.field = tk.Text(master=self.change_frame, bg="white", font=('Ariel', 11))
        self.field.pack(fill='both', expand=True)
        self.Notebook_bottom()

    def Notebook_bottom(self):
        options1 = ['Ariel', 'Times', 'Times New Roman']
        self.font = tk.StringVar()
        self.font.set('Ariel')
        options2 = ['11', '12', '16', '24']
        self.size = tk.StringVar()
        self.size.set('11')

        drop1 = tk.OptionMenu(self.bottom_left_frame, self.font, *options1)
        drop2 = tk.OptionMenu(self.bottom_left_frame, self.size, *options2)
        button = tk.Button(self.bottom_left_frame, text="Change")

        drop1.grid(row=0, column=0, padx= 100, pady= 75)
        drop2.grid(row=0, column=1, padx= 100)
        button.grid(row=0, column=2, padx= 100)

    def change_window_destroyer(self):
        for childen in self.change_frame.winfo_children():
            childen.destroy()

    def change_color_main(self):
        barva = colorchooser.askcolor()        
        self.main_frame.config(bg=str(barva[1]))

    def change_color_btnframe(self):
        barva = colorchooser.askcolor()
        self.button_frame.config(bg=str(barva[1]))

    def change_color_button(self):
        barva = colorchooser.askcolor()
        for childen in self.button_frame.winfo_children():
            childen.config(bg=str(barva[1]))

GUI()