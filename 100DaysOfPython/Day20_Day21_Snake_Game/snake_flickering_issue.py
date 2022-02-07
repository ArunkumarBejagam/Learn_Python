from turtle import Turtle

""" We have to define the constant names before the class name, and constant names always should be in capital 
    Constants are not allowed for modifications example you are not allowed to do (MOVE_DISTANCE += 10) """
SNAKE_SIZE = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes_list = []
        self.x_axis = 0
        self.y_axis = 0
        self.create_snake()
        self.head = self.snakes_list[0]
        self.new_snake_size = SNAKE_SIZE


    def create_snake(self):
        for i in range(SNAKE_SIZE):
            self.add_snake_segment(position=i)
            # self.x_axis -= 20

    def add_snake_segment(self, position):
        # self.snakes_list.append(position)
        # self.snakes_list[position] = Turtle(shape="square")
        # self.snakes_list[position].color("white")
        # self.snakes_list[position].penup()
        # self.snakes_list[position].goto(x=self.x_axis, y=self.y_axis)
        new_segement = Turtle(shape="square")
        new_segement.goto(x=self.x_axis, y=self.y_axis)
        new_segement.penup()
        new_segement.color("white")
        self.snakes_list.append(new_segement)

    def extend(self):
        self.add_snake_segment(self.new_snake_size)
        # self.snakes_list.append(self.new_snake_size)
        # self.snakes_list[self.new_snake_size] = Turtle(shape  ="square")
        # self.snakes_list[self.new_snake_size].penup()
        # self.snakes_list[self.new_snake_size].color("white")
        # x_pos = self.snakes_list[self.new_snake_size - 1].xcor()
        # y_pos = self.snakes_list[self.new_snake_size - 1].ycor()
        # self.snakes_list[self.new_snake_size].setpos(x=x_pos, y=y_pos)
        self.new_snake_size += 1

    def move(self):
        for i in range(len(self.snakes_list) - 1, 0, -1):
            x_position = self.snakes_list[i - 1].xcor()
            y_position = self.snakes_list[i - 1].ycor()
            self.snakes_list[i].goto(x=x_position, y=y_position)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

