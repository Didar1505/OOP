from turtle import Turtle

START_POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.head = None
        self.segments = []
        self.create_body()
    
    def create_segment(self, pos):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        return new_segment
    
    def create_body(self):
        for pos in START_POSITIONS:
            new_segment = self.create_segment(pos)
            self.segments.append(new_segment)
        self.head = self.segments[0]
    
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)
    
    def extend(self):
        new_segment = self.create_segment(self.segments[-1].pos())
        self.segments.append(new_segment)
    
    def up(self):
        if int(self.head.heading()) != 270:
            self.head.setheading(90)
    
    def down(self):
        if int(self.head.heading()) != 90:
            self.head.setheading(270)

    def left(self):
        if int(self.head.heading()) != 0:
            self.head.setheading(180)

    def right(self):
        if int(self.head.heading()) != 180:
            self.head.setheading(0)
            
    def reset(self):
        for each in self.segments:
            each.goto(1000, 1000)
        self.segments = []
        self.create_body()