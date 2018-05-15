import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your favorite op?")
answer = pg.prompt("Enter your favorite op below.")

if answer == "Mute":
    speak.Speak("Wow, that's my favorite too!")

elif answer == "Jäger":
    speak.Speak("You are too toxic for me. Please leave now.")

else:
    speak.Speak("Your favorite op is " + answer)

speak.Speak("What videos  do you want to watch")

video = pg.prompt("Enter video below.")

speak.Speak("Bet. Lets look for some " + video + "on YouTube")

wb.open("https://www.youtube.com/results?search_query=" + video)
