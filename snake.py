from turtle import Turtle
positions = [(0,0), (20, 0), (40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.create_body()
        self.head = self.segments[0]

    def create_body(self):
        for pos in positions:
            seg = Turtle(shape="square")
            seg.penup()
            seg.color('white')
            seg.goto(pos)
            self.segments.append(seg)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto((new_x,new_y))        

        self.segments[0].forward(20)
