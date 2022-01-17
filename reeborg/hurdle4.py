def turn_right():
    turn_left()
    turn_left()
    turn_left()
## Not efficient but works with less available conditions :

#def jump():
#    while not at_goal():
#        if front_is_clear():
#            move()
#            turn_right()
#        else:
#            turn_left()
#jump()


## Efficient methode.
def jump():
    while not at_goal():
        if wall_in_front() and wall_on_right():
            turn_left()
        elif front_is_clear() and wall_on_right(): 
            move()
        #elif front_is_clear() and wall_on_right() == False:
        else:
            turn_right()
            move()
            turn_right()
            move()
            
jump()
