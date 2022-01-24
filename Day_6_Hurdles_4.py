url = "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json"

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
  if wall_on_right() == True and front_is_clear() == True:
    move()
  elif wall_in_front() == True and right_is_clear() != True:
    turn_left()
  elif right_is_clear() == True:
    turn_right()
    move()   

while not at_goal():
  hurdle()


