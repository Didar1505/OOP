from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]
    
    def create_body(self):
        for pos in positions:
            seg = self.create_segment(pos)
            self.segments.append(seg)

    def create_segment(self, pos):
        seg = Turtle(shape='square')
        seg.color("white")
        seg.penup() 
        seg.goto(pos)
        return seg
    
    def move(self):
        for i in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def append(self):
        x_cor = self.segments[-1].xcor()
        y_cor = self.segments[-1].ycor()
        pos = (x_cor, y_cor)
        seg = self.create_segment(pos)
        self.segments.append(seg)