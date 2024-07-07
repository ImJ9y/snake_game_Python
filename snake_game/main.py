import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("MY Snake Game")
Screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

Screen.update()

Screen.listen()
Screen.onkey(snake.up, "Up")
Screen.onkey(snake.down, "Down")
Screen.onkey(snake.left, "Left")
Screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    Screen.update()
    time.sleep(.1)
    snake.move()

    #detect collision with food
    #with distance comparing two different turtles
    if snake.head.distance(food) < 15:
        food.refresh()
        Screen.update()
        snake.extend()
        scoreboard.scored()

    #when snake hits the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tall
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    #slicing - piano_keys = a~g -> piano_keys[2,5]
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

Screen.exitonclick()