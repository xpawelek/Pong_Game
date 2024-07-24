from turtle import Turtle

FONT_SIZE = 30
class Scoreboard(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.score = 0
        self.goto(0,0)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(pos_x, pos_y - FONT_SIZE)
        self.refresh()

    def refresh(self):
        self.write(f"{self.score}", font=("Verdana", FONT_SIZE, "bold"))