from turtle import Turtle

class Score(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.color("white")
        self.left_player = 0
        self.right_player = 0
        self.penup()
        self.goto(0, 230)
        self.draw()
        
    def draw(self):
        self.write(f"{self.left_player} : {self.right_player}", align='center', font=("Monospace", 34, "bold"))

    def update(self):
        self.clear()
        self.draw()
    