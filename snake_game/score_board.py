from turtle import Turtle
()
class Score(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 250)
        self.draw()
        
    def draw(self):
        self.clear()
        self.write("Score: " + str(self.score), align='center', font=('Arial', 24, 'normal'))
        
    def update(self):
        self.score += 1
        self.draw()
    
    def restart(self):
        self.score = 0
        self.draw()