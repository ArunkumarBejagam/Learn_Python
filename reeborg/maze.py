def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#while not at_goal():
#    if wall_in_front() and wall_on_right():
#        turn_left()
#    elif front_is_clear() and wall_on_right(): 
#        move()
#    else:
#        turn_right()
#        move()

while not at_goal():
    if wall_in_front() and wall_on_right()==False:
        turn_right()
        move()
    elif wall_in_front() == False and wall_on_right()==False:
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    

    
