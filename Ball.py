from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed(1)

    def move(self):
        self.forward(10)

    def ball_refresh(self):
        self.home()
        if_invert = random.choice([True, False])
        if if_invert:
            self.invert_direction()
    def invert_direction(self):
        new_val = (self.heading() + 180) % 360
        #print(new_val)
        self.setheading(int(new_val))

    def hit_box(self):
        left_or_right = random.choice(['left', 'right'])

        if left_or_right == 'left':
            self.left(random.randint(0, 45))
        else:
            self.right(random.randint(0, 45))

    def hit_bottom_wall(self):
        self.setheading(random.randint(0, 45))

    def hit_top_wall(self):
        self.right(random.randint(0, 45))


    def ball_hits_up_or_down(self, side, direction):
        print("xxx")
        if side == 'up':
            if direction == 'left':
                self.setheading(random.randint(185, 220))
                print("lewo gora")
            elif direction == 'right':
                print("prawo gora")
                self.setheading(random.randint(325, 355))
        elif side == 'down':
            if direction == 'left':
                print("lewo dol")
                self.setheading(random.randint(140, 175))
            elif direction == 'right':
                print("prawo dol")
                self.setheading(random.randint(0, 45))


