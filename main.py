from random import randint
from tkinter import *
import time

class Starship:
    def __init__(self):
        size = 20
        self.center = (tk.winfo_width() // 2, tk.winfo_height() // 2,
                       tk.winfo_width() // 2, tk.winfo_height() // 2)
        self.ship = canvas.create_rectangle(self.center[0] - size, self.center[1] - size,
                                            self.center[2] + size, self.center[3] + size, fill='yellow')
        self.speed = 15
        self.x_speed = 0
        self.y_speed = -5
        canvas.bind_all("<Up>", self.up)
        canvas.bind_all("<Down>", self.down)
        canvas.bind_all("<Left>", self.left)
        canvas.bind_all("<Right>", self.right)

    def move(self):
        canvas.move(self.ship, self.x_speed, self.y_speed)
        cords = canvas.coords(self.ship)
        if cords[0] >= tk.winfo_width():
            canvas.move(self.ship, -tk.winfo_width(), 0)
        if cords[1] >= tk.winfo_height():
            canvas.move(self.ship, 0, -tk.winfo_height())
        if cords[2] <= 0:
            canvas.move(self.ship, tk.winfo_width(), 0)
        if cords[1] <= 0:
            canvas.move(self.ship, 0, tk.winfo_height())

    def up(self, _):
        if self.y_speed == -self.speed:
            self.x_speed = 0
        self.y_speed = -self.speed

    def down(self, _):
        if self.y_speed == self.speed:
            self.x_speed = 0
        self.y_speed = self.speed

    def left(self, _):
        if self.x_speed == -self.speed:
            self.y_speed = 0
        self.x_speed = -self.speed

    def right(self, _):
        if self.x_speed == self.speed:
            self.y_speed = 0
        self.x_speed = self.speed

class Asteroid:
    def __init__(self):
        self.asteroids = [canvas.create_oval(-30, y := randint(0, tk.winfo_height()),
                                             size := randint(10, 30), y + size, fill='brown') for _ in range(10)]

    def move(self):
        for ast in self.asteroids:
            canvas.move(ast, 10, randint(0, 10))

def close():
    global keep_going
    tk.destroy()
    keep_going = False

tk = Tk()
tk.wm_attributes("-topmost", 1)
tk.title("Лабораторная работа 3.4")
tk.resizable(False, False)
tk.wm_protocol("CLOSE_WINDOW", close)

canvas = Canvas(tk, width=500, height=500, bg='grey22')
for _ in range(randint(50, 100)):
    canvas.create_oval(x := randint(0, 500), y := randint(0, 500), x + 1, y + 1, fill='white')
canvas.pack()
tk.update()

keep_going = True
ship = Starship()
asteroids = Asteroid()
#draw_all(ship)

#tk.mainloop()

while keep_going:
    ship.move()
    asteroids.move()
    time.sleep(0.05)
    tk.update()
