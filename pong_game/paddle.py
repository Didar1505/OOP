from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=0.5, stretch_wid=5)
        self.goto(pos)
    
    def up(self):
        if self.ycor() < 250:
            print(self.ycor())
            self.goto(self.xcor(), self.ycor() + 50)
    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 50)
    