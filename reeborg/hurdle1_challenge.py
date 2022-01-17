def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
i = 1   
for i in range(1,number_of_hurdles+1):
    jump_hurdle()
    i+=1
