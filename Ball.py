from turtle import Turtle
import random
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed("fastest")

    def move(self):
        self.forward(10)

    def refresh(self):
        self.home()
        if_invert = random.choice([True, False])
        if if_invert:
            self.invert_direction()
    def invert_direction(self):
        new_val = (self.heading() + 180) % 360
        self.setheading(int(new_val))

    def hits_paddle(self):
        left_or_right = random.choice(['left', 'right'])

        if left_or_right == 'left':
            self.left(random.randint(0, 45))
        else:
            self.right(random.randint(0, 45))

    def ball_hits_top_or_bottom(self, side, direction):

        if side == 'top':
            if direction == 'left':
                self.setheading(random.randint(185, 220))
            elif direction == 'right':
                self.setheading(random.randint(325, 355))
        elif side == 'bottom':
            if direction == 'left':
                self.setheading(random.randint(140, 175))
            elif direction == 'right':
                self.setheading(random.randint(0, 45))


