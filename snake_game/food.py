from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green')
        self.penup()
        self.update()

    def update(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 250)
        self.goto(new_x, new_y)
