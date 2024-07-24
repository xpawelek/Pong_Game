from turtle import Turtle

DOWN = False
UP = False
class Player(Turtle):
    def __init__(self, x_cord):
        super().__init__()
        self.close_to_wall = False
        self.paddle = []
        self.x_cord = x_cord
        self.create_paddle()
        self.head = self.paddle[0]
        self.tail = self.paddle[-1]


    def create_paddle(self):
        y_cord = 30
        for i in range(5):
            part_of_paddle = Turtle()
            part_of_paddle.shape("square")
            part_of_paddle.shapesize(1)
            part_of_paddle.penup()
            part_of_paddle.color("white")
            part_of_paddle.goto(self.x_cord, y_cord)
            y_cord = y_cord - 20
            self.paddle.append(part_of_paddle)



#ogarnac paddle
    def going_up(self):
        for i in range(len(self.paddle) - 1, 0, -1):
            self.paddle[i].setpos(self.paddle[i - 1].xcor(), self.paddle[i - 1].ycor())
        self.head.sety(self.head.ycor() + 20)



    def players_touches_up(self):
        for i in range(0, len(self.paddle) - 1):
            self.paddle[i].setpos(self.paddle[i + 1].xcor(), self.paddle[i + 1].ycor())
        self.tail.sety(self.tail.ycor() - 20)

    def players_touches_bottom(self):
        for i in range(len(self.paddle) - 1, 0, -1):
            self.paddle[i].setpos(self.paddle[i - 1].xcor(), self.paddle[i - 1].ycor())
        self.head.sety(self.head.ycor() + 20)

    def going_down(self):
        for i in range(0, len(self.paddle) - 1):
            self.paddle[i].setpos(self.paddle[i + 1].xcor(), self.paddle[i + 1].ycor())
        self.tail.sety(self.tail.ycor() - 20)


    def player_gets_point(self, scoreboard):
        scoreboard.score += 1
        scoreboard.clear()
        scoreboard.refresh()