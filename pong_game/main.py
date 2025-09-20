from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()



p_right_pos = (420, 0)
p_left_pos = (-430, 0)
speed = 0.03
p_right = Paddle(p_right_pos)
p_left = Paddle(p_left_pos)
score = Score()
ball = Ball()

# BIND KEYS
screen.onkey(p_right.up, 'Up')
screen.onkey(p_right.down, "Down")
screen.onkey(p_left.up, "w")
screen.onkey(p_left.down, 's')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    
    # RIGHT PADDLE
    if (ball.xcor() > 400 and ball.distance(p_right) < 50):
        ball.bounce_paddle()

    # LEFT PADDLE
    if (ball.xcor() < -400 and ball.distance(p_left) < 50):
        ball.bounce_paddle()

    if ball.xcor() > 450:
        score.left_player += 1
        score.update()
        ball.reset()
        p_right.goto(p_right_pos)
        time.sleep(2)
        
    elif ball.xcor() < -450:
        score.right_player += 1
        score.update()
        ball.reset()
        p_left.goto(p_left_pos)
        time.sleep(2)


    

screen.exitonclick()