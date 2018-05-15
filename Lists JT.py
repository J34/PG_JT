import random

name = "Jack Turk"

characters = ["Jager","Bandit","Blitz","IQ","Thermite","Ash","Castle","Pulse","Tachanka","Glaz","Fuze","Kapkan","Rook","Twitch","Montagne","Doc","Mute","Thatcher","Smoke","Sledge","Buck","Frost","Capitao","Caviera","Valkyrie","Blackbeard","Hibana","Echo","Vigil","Dokkaebi","Ela","Zofia","Recruit","Mira","Jackal","Lesion","Ying",]

print("Hello " + name)


print(characters[random.randint(0,37)])


movies = []

while True:
    print("What's one of your favorite movies? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break

