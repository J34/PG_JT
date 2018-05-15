import random

number = random.randint(0,3)

words = ["Buck","Lion","Frost","Echo"]

hint1 = ["Bronco","King","Bear","Repeat"]

hint2 = ["Skeleton Key","EE-ONE-D","99m","Yokai"]

guess = ""

counter = 1

secretword = words[number]

while True:
    print("Guess the Operator!")
    print("Type 'hint1', 'hint2', 'first letter', 'last letter', or 'give up' for help")
    guess = input()

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses!")
        break

    elif guess == "hint1":
        print( hint1[number]  )

    elif guess == "hint2":
        print( hint2[number]  )

    elif guess == "first letter":
        print( secretword[0]  )

    elif guess == "last letter":
        print( secretword[-1])

    elif guess == "give up":
        print("The word was " + secretword)
        break

    else:
        print("Try Again!")
        counter += 1
