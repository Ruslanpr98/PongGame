from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left = 0
        self.right = 0
        self.show_score()


    def show_score(self):

        self.goto(-100,200)
        self.write(self.left, align="center", font=("Courier", 40, "normal"))
        self.goto(100,200)
        self.write(self.right, align="center", font=("Courier", 40, "normal"))


    def left_score(self):
        self.left += 1
        self.clear()
        self.show_score()

    def right_score(self):
        self.right += 1
        self.clear()
        self.show_score()