'''
player class - position, rectangle
net_class ? middle
ball_class - +1 for any player if back, moving, bouncing from players
score_board class - score left right
'''
import turtle
from turtle import Turtle, Screen
from Scoreboard import Scoreboard
from Ball import Ball
from Player import Player
import time

screen = Screen()
screen_width = 1000
screen_height = 650
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)
screen.bgcolor('black')

#net
net = Turtle()
net.penup()
net.hideturtle()
net.color('white')
half_of_height = (screen_height // 2) - 20
net.goto(0, half_of_height)
net.setheading(270)
net_drawing_start = 0
i = 0
while net_drawing_start <= 2*half_of_height:
    if i % 2 == 0:
        net.pendown()
    else:
        net.penup()
    net.forward(10)
    net_drawing_start += 10
    i += 1

#players

player_1_x_cord = (screen_width // 2) - 25
player_2_x_cord = -(screen_width // 2) + 25
player_1 = Player(player_1_x_cord, screen)
player_2 = Player(player_2_x_cord, screen)

screen.listen()
screen.onkeypress(player_1.move_up, "Up")
screen.onkeyrelease(player_1.stop_move_up, "Up")
screen.onkeypress(player_1.move_down, "Down")
screen.onkeyrelease(player_1.stop_move_down, "Down")

screen.onkeypress(player_2.move_up, "w")
screen.onkeyrelease(player_2.stop_move_up, "w")
screen.onkeypress(player_2.move_down, "s")
screen.onkeyrelease(player_2.stop_move_down, "s")


#ball
ball = Ball()

#scoreboards
#scoreboard first player
distance_from_middle = 100
scoreboard_first_player = Scoreboard(distance_from_middle, half_of_height)

#scoreboard second player
scoreboard_second_player = Scoreboard(-distance_from_middle - 25, half_of_height)

#playing game
game_active = True
from_left = False
from_right = False
direction = ""

while game_active:
    time.sleep(0.02)

    ball.move()

    if player_1.head.ycor() >= half_of_height + 20:
        player_1.touches_up()

    if player_1.tail.ycor() <= (-1 * half_of_height) - 20:
        player_1.touches_bottom()

    if player_2.head.ycor() >= half_of_height + 20:
        player_2.touches_up()

    if player_2.tail.ycor() <= (-1 * half_of_height) - 20:
        player_2.touches_bottom()

    screen.update()

    for paddle in player_1.paddle:
        if ball.distance(paddle) < 20:
            direction = "left"
            ball.invert_direction()
            ball.forward(10)
            ball.hits_paddle()
            break

    for paddle in player_2.paddle:
        if ball.distance(paddle) < 20:
            direction = "right"
            ball.invert_direction()
            ball.forward(10)
            ball.hits_paddle()
            break

    if ball.ycor() >= screen_height // 2 - 10:
        ball.ball_hits_top_or_bottom("top", direction)
    if ball.ycor() <= -half_of_height:
        ball.ball_hits_top_or_bottom("bottom", direction)

    if ball.xcor() >= screen_width // 2:
        player_2.gets_point(scoreboard_second_player)
        ball.refresh()
        screen.update()
        time.sleep(0.5)

    if ball.xcor() <= -screen_width // 2:
        player_1.gets_point(scoreboard_first_player)
        ball.refresh()
        screen.update()
        time.sleep(0.5)


screen.exitonclick()

