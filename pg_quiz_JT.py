import pyautogui as pg
import time
import webbrowser
points=0

#Question goes here
answer = pg.prompt(
"""
A friend of yours is being bullied. What do you do?

a)Fight the bully
b)Try to talk to the bully
c)Tell on the bully
d)Do nothing

"""
    )

pg.alert("You chose " + answer)

# answer and points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4

#Question goes here
answer = pg.prompt(
"""
Somebody is trying to fight you and you are hiding. You know they know where they are. What do you do?

a)Prepare yourself for the fight
b)Plan a trap
c)Call a friend to fight him for you
d)Stay and get beat up

"""
    )

pg.alert("You chose " + answer)

# answer and points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4

#Question goes here
answer = pg.prompt(
"""
A friend needs your help, but if you help them you will get in trouble. What do you do?

a)Don't help them and laugh at them when they fail
b)Plan something out that will get him out of trouble without you getting in trouble
c)Tell him to go to another friend
d)Help them and get in trouble

"""
    )

pg.alert("You chose " + answer)

# answer and points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4

#Question goes here
answer = pg.prompt(
"""
Somebody is annoying you. What do you do?

a)Beat the person up
b)Tell the person they are annoying
c)Get someone else to tell him to stop/fight him
d)Do nothing

"""
    )

pg.alert("You chose " + answer)

# answer and points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4

#Question goes here
answer = pg.prompt(
"""


a)Fight the bully
b)Try to talk to the bully
c)Tell on the bully
d)Do nothing

"""
    )

pg.alert("You chose " + answer)

# answer and points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4





# END OF SURVEY
pg.alert("Your character is...")
#Toxic Player
if points < 6:
    pg.alert("You are toxic!")
    webbrowser.open("https://i.ytimg.com/vi/xLoTSpZy344/maxresdefault.jpg")
#Trapper
elif points > 7 and points <=11:
    pg.alert("You are should main trap operators")
    webbrowser.open("https://cdn.images.express.co.uk/img/dynamic/143/590x/rainbow-six-siege-636416.jpg")
#Camper
elif points > 12 and points <=16:
    pg.alert("You are a camper!")
    webbrowser.open("https://i.redd.it/ogbtmi5iwr6y.png")
#Recruit
elif points > 17 and points <=21:
    pg.alert("You shouldn't be playing R6 Siege")
    webbrowser.open("https://www.youtube.com/watch?v=oP_Glkszdiw")
