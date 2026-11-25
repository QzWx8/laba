from random import randint
from tkinter import *

class Starship:
    def __init__(self):
        size = 20
        self.center = (tk.winfo_width() // 2, tk.winfo_height() // 2,
                       tk.winfo_width() // 2, tk.winfo_height() // 2)
        self.ship = canvas.create_rectangle(self.center[0] - size, self.center[1] - size,
                                            self.center[2] + size, self.center[3] + size, fill='yellow')
        self.speed = 30
        self.x_speed = 0
        self.y_speed = 5
        self.move()
        canvas.bind_all("<Up>", self.up)
    
    def move(self):
        canvas.move(self.ship, self.x_speed, self.y_speed)
    
    def up(self, _):
        self.y_speed = self.speed
    
    def down(self, _):
        self.y_speed = -self.speed
    
    def left(self, _):
        self.x_speed = -self.speed
    
    def right(self, _):
        pass
        

tk = Tk()
tk.wm_attributes("-topmost", 1)
tk.title("Лабораторная работа 3.4")
tk.resizable(False, False)
tk.wm_protocol("CLOSE_WINDOW", tk.destroy)

canvas = Canvas(tk, width=500, height=500, bg='grey22')
for _ in range(randint(50, 100)):
    canvas.create_oval(x:=randint(0, 500), y:=randint(0, 500), x+1, y+1, fill='white')
canvas.pack()
tk.update()

ship = Starship()
print(tk.winfo_width(), canvas.winfo_width())

tk.mainloop()
