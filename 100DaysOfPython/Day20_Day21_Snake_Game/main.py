from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("My Snake Game !")
my_screen.setup(height=600, width=600)
my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score = ScoreBoard()

my_screen.update()

my_screen.listen()
my_screen.onkey(key="Up", fun=my_snake.up)
my_screen.onkey(key="Down", fun=my_snake.down)
my_screen.onkey(key="Left", fun=my_snake.left)
my_screen.onkey(key="Right", fun=my_snake.right)

# my_screen.update()
game_is_on = True
#
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detect collision with food
    if my_snake.head.distance(my_food) < 15:
        print("I got it 😋")
        my_food.refresh_food()
        my_snake.extend()
        # my_screen.update()
        my_score.update_score()

    # Detect collision with Wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        my_score.collision()
        game_is_on = False

    # Detect collision with tail
    # for segment in my_snake.snakes_list:
    #     if my_snake.head.distance(segment) < 10 and segment != my_snake.head:
    #         my_score.collision()
    #         game_is_on = False

    for segment in my_snake.snakes_list[1:]:
        if my_snake.head.distance(segment) < 10:
            my_score.collision()
            game_is_on = False

my_screen.exitonclick()


## Based on the input randomly increase the snake speed and reduce the speed during the game.
## Change snake shape.

