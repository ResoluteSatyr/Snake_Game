# Create a program that emulates the Snake Game
from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Turns animation on and off
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    # It updates the screen to show more content
    screen.update()
    # IT adds a delay to the screen animation
    time.sleep(0.1)
    snake.move()
    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # Detect Collision with Wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # game_is_on = False
        # score.game_over()
        score.reset_score()
        snake.reset_snake()
        continue
    # Detect Collision with Tail
    """This will start counting the list from the second item to last"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score.reset_score()
            snake.reset_snake()


screen.exitonclick()
