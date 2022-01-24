url = "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def escape():
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    elif wall_in_front() == True and wall_on_right() == True:
        turn_left()
    elif front_is_clear() == True and right_is_clear() == True:
        turn_right()

while not at_goal():
    escape()