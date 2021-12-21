from turtle import Screen, xcor, ycor
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
game_is_on = True

screen.bgcolor("black")
screen.setup(width= 800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

# Move left paddle
screen.onkeypress(key="w", fun= l_paddle.move_up)
screen.onkeypress(key="s",fun=  l_paddle.move_down)

# Move right paddle
screen.onkeypress(key="Up", fun= r_paddle.move_up)
screen.onkeypress(key="Down",fun=  r_paddle.move_down)

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper and lower wall and change direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    elif ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

















screen.exitonclick()