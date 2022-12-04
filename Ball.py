from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=2,stretch_len=2)
        self.penup()
        self.goto(position)
        self.x = 0.15
        self.y = 0.15

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1