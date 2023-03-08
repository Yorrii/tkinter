import tkinter as tk
import random

class Snake_Game():
    def __init__(self):
        self.root = tk.Tk()     # Creating main window
        self.root.withdraw()    # Make main window invisible
        self.topWindow = tk.Toplevel(self.root) # top level window to get entries
        self.topWindow.title("Snake Game Menu") 
        self.topWindow.geometry("700x400")
        self.topWindow.attributes('-topmost', 'true')   # makes the top window do overdraw other windows

        self.speedLable = tk.Label(self.topWindow, text='Set snake speed:', font=('Ariel', 16)) # Create lable
        self.speedLable.grid(row=0, column = 0, padx= 100, pady = 25) # set the position of the lable to row, column using grid
        
        self.speedEntry = tk.Entry(self.topWindow, fg="gray", font=('Ariel', 16))   # Creating entry window for snake speed
         # Setting default text to be 200 inside of snake speed entry
         # binding snake speed entry to remove text inside if clicked
        self.speedEntry.grid(row=0, column = 1) # placing the entry to first row, second column next to its lable

        self.widthLable = tk.Label(self.topWindow, text='Set width of fields:', font=('Ariel', 16))
        self.widthLable.grid(row=1, column = 0, pady = 25)

        self.widthEntry = tk.Entry(self.topWindow, fg="gray", font=('Ariel', 16))
        #
        #
        self.widthEntry.grid(row=1, column = 1)

        self.heightLable = tk.Label(self.topWindow, text='Set height of fields:', font=('Ariel', 16))
        self.heightLable.grid(row=2, column = 0, pady = 25)

        self.heightEntry = tk.Entry(self.topWindow, fg="gray", font=('Ariel', 16))
        #
        #
        self.heightEntry.grid(row=2, column = 1)

        self.button = tk.Button(self.topWindow, text="Start the GAME", font=('Ariel', 16), height=3, command=self.startGame)
        self.button.grid(row=3, column=0, columnspan=2)



    def startGame(self): # příprava pro start hry
         # get text from entry widget
         # get text from entry widget
         # get text from entry widget
        self.square_size = 20

        # bind window to change snake direction by pressing up, down, left, right
        #
        #
        #
        
        self.canvas = tk.Canvas(self.root, bg="black",
                                 height= self.height*self.square_size,
                                   width= self.width*self.square_size)
        self.canvas.pack() # packing the canvas to main window using pack

        self.snake = Snake()
        self.fruit = Fruit()
        self.draw_start()
        self.game_round()

        self.root.deiconify() # main window reapear
        self.topWindow.destroy()

    def game_round(self): # hlavní metoda pro hru
        x, y = self.snake.coordinates[0]

        if self.snake.direction == "left":
            x -= self.square_size
        elif self.snake.direction == "right":
            x += self.square_size
        elif self.snake.direction == "up":
            y -= self.square_size
        elif self.snake.direction == "down":
            y += self.square_size

        square = self.canvas.create_rectangle(x, y, x+20, y+20, fill= self.snake.color)

        self.snake.coordinates.insert(0, [x, y])
        self.snake.squares.insert(0, square)
        
        if x == self.fruit.coordinates[0] and y == self.fruit.coordinates[1]: # if pro snězení ovoce
            self.canvas.delete(self.fruit_oval)
            self.fruit.set_coordinates(int(self.width)*self.square_size,
                                        int(self.height)*self.square_size, self.square_size)
            self.fruit_oval = self.canvas.create_oval(self.fruit.coordinates[0], self.fruit.coordinates[1],
                                                      self.fruit.coordinates[0]+self.square_size,
                                                        self.fruit.coordinates[1]+self.square_size, fill=self.fruit.color)
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_for_collision():
            self.game_over()
        else:        
            # next iteration of the game (self.speed, self.next_turn)


    def draw_start(self): # vykreslení startu
        
        self.fruit.set_coordinates(self.width*self.square_size, self.height*self.square_size, self.square_size)

        a, b = self.fruit.coordinates[0], self.fruit.coordinates[1]

        self.fruit_oval = self.canvas.create_oval(a, b, a+self.square_size, b+self.square_size, fill=self.fruit.color)
        for x, y in self.snake.coordinates:
            square = self.canvas.create_rectangle(x, y, x+20, y+20, fill= self.snake.color)
            self.snake.squares.append(square)

    def check_for_collision(self): # zkontrolování nárazu
        x, y = self.snake.coordinates[0]

        if 0>x or x>=self.width*20 or 0>y or y>=self.height*20:
            return True
        for i in range(1,len(self.snake.coordinates)):
            a, b = self.snake.coordinates[i]
            if x == a and y == b:
                return True  

        return False
    
    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(self.width*self.square_size/2, # vykreslení textu při naražení
                       self.height*self.square_size/2,
                       font=('consolas', 50), 
                       text="GAME OVER", 
                       fill="red", tag="gameover")


class Snake:
    def __init__(self):
        self.color = "lime"
        self.bodysize = 3
        self.coordinates = []
        self.squares = []
        self.color = "#3dc461"
        self.direction = "right"
        

        for i in range(self.bodysize):
            self.coordinates.append([0, 0])

    def change_direction(self, new_direction):
          
        if new_direction == "up": 
            if self.direction != "down":
                self.direction = "up"
        elif new_direction == "down":
            if self.direction != "up":
                self.direction = "down"
        elif new_direction == "left":
            if self.direction != "right":
                self.direction = "left"
        elif new_direction == "right":
            if self.direction != "left":
                self.direction = "right"


class Fruit:
    def __init__(self):
        self.color="#ed7e28"
        self.coordinates = []

    def set_coordinates(self, width, height, body_size):
        self.coordinates = []
        x = random.randrange(0, width, body_size)
        self.coordinates.append(x)

        y = random.randrange(0, height, body_size)
        self.coordinates.append(y)
        