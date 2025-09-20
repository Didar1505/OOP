from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color('white')
        self.shape('circle')
        self.penup()
        self.game_is_on = True
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_x = self.xcor()  + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_wall(self):
        self.y_move *= -1
    def bounce_paddle(self):
        self.x_move *= -1
        self.move()
        
    def reset(self):
        self.goto(0,0)