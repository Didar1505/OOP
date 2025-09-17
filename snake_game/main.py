from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import Score

TICK_MS = 100

screen = Screen()
screen.setup(width=600,height=600)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)
screen.bgcolor('black')
screen.tracer(0)
screen.title("My Snake Game")
screen.listen()

# GAME STATE
snake = None
food = None
score = None
running = None

msg = Turtle(visible=False)
msg.color('red')
msg.penup()

def show_message(text, color='red', y=0):
    msg.clear()
    msg.color(color)
    msg.goto(0, y)
    msg.write(text, align='center', font=("Monospace", 24, 'bold'))

def bind_keys():
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkey(restart, 'r')
    screen.onkey(restart, 'R')

def start_game():
    global snake, food, score, running
    if snake is None:
        snake = Snake()
    else:
        snake.reset()
    
    if food is None:
        food = Food()
    else:
        food.update()
    
    if score is None:
        score = Score()
    else:
        score.restart()
    show_message("")
    bind_keys()
    running = True
    screen.update()
    screen.ontimer(game_step, TICK_MS)
    
def game_over():
    """Stop ticking and display message."""
    global running
    running = False
    show_message("Game Over!\nPress R to restart", y=20)
    screen.update()
    
def game_step():
    """One tick of the game."""
    if not running:
        return

    snake.move()

    # FOOD COLLISION
    if snake.head.distance(food) < 20:
        snake.extend()
        if hasattr(food, 'update'):
            food.update()
        score.update()

    # WALL COLLISION (±280 for a 600×600 playfield with margin)
    x, y = snake.head.xcor(), snake.head.ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        return game_over()

    # TAIL COLLISION (skip head; use distance not exact pos)
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            return game_over()

    screen.update()
    screen.ontimer(game_step, TICK_MS)

def restart():
    """Restart the game when 'R' is pressed."""
    start_game()
    
start_game()

screen.exitonclick()