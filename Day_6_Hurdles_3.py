url ="https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json"

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#=================================================
# SOLUTION 1
while at_goal() != True:
    if wall_in_front():
        hurdle()
    else:
        move()

#=================================================
# SOLUTION 2
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
