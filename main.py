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
player_1 = Player(player_1_x_cord)
player_2 = Player(player_2_x_cord)

screen.listen()
screen.onkeypress(key="Up", fun=player_1.going_up)
screen.onkeypress(key="Down", fun=player_1.going_down)
screen.onkeypress(key="w", fun=player_2.going_up)
screen.onkeypress(key="s", fun=player_2.going_down)

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
        player_1.players_touches_up()

    if player_1.tail.ycor() <= (-1 * half_of_height) - 20:
        player_1.players_touches_bottom()

    if player_2.head.ycor() >= half_of_height + 20:
        player_2.players_touches_up()

    if player_2.tail.ycor() <= (-1 * half_of_height) - 20:
        player_2.players_touches_bottom()

    screen.update()

    for paddle in player_1.paddle:
        if ball.distance(paddle) < 20:
            direction = "left"
            paddle.color("red")
            ball.invert_direction()
            ball.forward(10)
            ball.hit_box()
            break

    for paddle in player_2.paddle:
        if ball.distance(paddle) < 20:
            direction = "right"
            ball.invert_direction()
            ball.forward(10)
            ball.hit_box()
            break


    if ball.ycor() >= screen_height // 2 - 10:
        print(direction)
        ball.ball_hits_up_or_down("up", direction)
    if ball.ycor() <= -half_of_height:
        print(direction)
        ball.ball_hits_up_or_down("down", direction)


    if ball.xcor() >= screen_width // 2:
        player_2.player_gets_point(scoreboard_second_player)
        ball.ball_refresh()

    if ball.xcor() <= -screen_width // 2:
        player_1.player_gets_point(scoreboard_first_player)
        ball.ball_refresh()

screen.exitonclick()

