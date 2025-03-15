from turtle import Turtle, Screen

DOWN = False
UP = False
class Player(Turtle):
    def __init__(self, x_cord, screen):
        super().__init__()
        self.close_to_wall = False
        self.paddle = []
        self.x_cord = x_cord
        self.moving_up = False
        self.moving_down = False
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

    def move_up(self):
        if not self.moving_up:
            self.moving_up = True
            self.smooth_move("up")

    def move_down(self):
        if not self.moving_down:
            self.moving_down = True
            self.smooth_move("down")

    def stop_move_up(self):
        self.moving_up = False

    def stop_move_down(self):
        self.moving_down = False

    def smooth_move(self, direction):
        if direction == "up" and self.moving_up and self.head.ycor() < 300:
            for segment in reversed(self.paddle):
                segment.sety(segment.ycor() + 5)
            self.screen.ontimer(lambda: self.smooth_move("up"), 10)

        elif direction == "down" and self.moving_down and self.tail.ycor() > -300:
            for segment in self.paddle:
                segment.sety(segment.ycor() - 5)
            self.screen.ontimer(lambda: self.smooth_move("down"), 10)

    def touches_up(self):
        for i in range(0, len(self.paddle) - 1):
            self.paddle[i].setpos(self.paddle[i + 1].xcor(), self.paddle[i + 1].ycor())
        self.tail.sety(self.tail.ycor() - 20)

    def touches_bottom(self):
        for i in range(len(self.paddle) - 1, 0, -1):
            self.paddle[i].setpos(self.paddle[i - 1].xcor(), self.paddle[i - 1].ycor())
        self.head.sety(self.head.ycor() + 20)

    def gets_point(self, scoreboard):
        scoreboard.score += 1
        scoreboard.clear()
        scoreboard.refresh()