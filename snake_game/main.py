from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()


screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

speed = 0.08
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)

    snake.move()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300:
        game_is_on = False
    elif snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_is_on = False

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.append()
        speed -= 0.005
    
    for seg in snake.segments[1:]:
        if snake.head.pos() == seg.pos():
            game_is_on = False

screen.exitonclick()