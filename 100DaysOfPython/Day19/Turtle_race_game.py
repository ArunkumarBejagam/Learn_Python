import random
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=600, height=500)
is_game_started = False
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
play_game = True
user_bet = my_screen.textinput(title="Make your bet",
                               prompt="Which turtle will win the raise? Enter a colour: ").lower()

# If user enters a valid turtle color as a input, then race will start.

while play_game:
    if user_bet == "stop_game":
        play_game = False
        my_screen.bye()
    elif user_bet in colors:
        play_game = False
        is_game_started = True
    else:
        user_bet = my_screen.textinput(title="Enter wrong choice, Please enter again",
                                       prompt=" Please select a valid turtle color ").lower()
# print(user_bet)

random.shuffle(colors)
turtle_names = []

print(turtle_names)
print(colors)

x_axis = -280
y_axis = -100
different_lengths = [10, 15, 20, 25, 30]
distance_traveled = 0

# using below for loop, we are creating 7 turtles (turtle_names[0], turtle_names[1] so on, turtle_names[6])
for i in range(7):
    turtle_names.append(i)
    turtle_names[i] = Turtle(shape="turtle")
    turtle_names[i].color(colors[i])
    turtle_names[i].penup()
    turtle_names[i].goto(x_axis, y_axis)
    y_axis += 30

distance_traveled = 0

#while loop will start once user enters some value and race will continue till one of the turtle reaches end of the screen (end of th x axis)     
while is_game_started:
    for i in range(len(turtle_names)):
        if turtle_names[i].xcor() > 270:
            is_game_started = False
            winner_color = turtle_names[i].color()[0]
            # turtle_names[i].color()[0], turtle.color will give us 2 colors, one is body color and other is pen color. So to display only body color used [0]
            if winner_color.lower() == user_bet.lower():
                print("You've won 😁!")
            else:
                print("You've lost ☹️")
            print(f"Winner is {winner_color}")
        else:
            turtle_names[i].forward(random.randint(0, 10))

        # if distance_traveled > 270:




my_screen.exitonclick()
