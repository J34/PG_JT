import pyautogui as pg
import time
import webbrowser
points=0

#Question goes here
answer = pg.prompt(
"""
A teammate of your is telling your friend that they are bad. What do you do

a)Teamkill them
b)Force him out of the objective
c)Report him for toxic behavior
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
Somebody is trying to kill you and you are hiding. You know they know where you are, but you don't know where they are. What do you do?

a)Prepare yourself for the fight
b)Plan a trap
c)Ask a friend to fight him for you
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
A teammate is cornered. If you help them, you will probably die. What do you do?

a)Help the enemies get them
b)Plan something out that will get him out of trouble without you getting in trouble
c)Tell him to go to ask another teammate
d)Help them and get in killed

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
A teammate keeps teamkilling. What do you do?

a)Teamkill them
b)Tell them to stop
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
You are cornered in a 2 v 1. What do you do?

a)Run and Gun
b)Wait for them to push while holding a nitro cell
c)Try to move to a different spot
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
