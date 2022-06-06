import random
 
# Scripts start here for variables
# Learning for something simple :)
# Created by Steven (@keritzy)

randomN = 10 #// random.randint(1,100) 1 til 100
print(randomN)
gameR = True
numbersG = []
tries = 0
 
# Starting up the game 
print("This is just a simple guessing game .")
playerN = input("You need to input your name? ")
print("Hello, " + playerN)
print("We play guess game.")
print("Guess a number from 1 - 100")
print("----------------------------------------")
print("If you need HELP type H")
print("----------------------------------------")
 
# Game loop // Game Random
while gameR :
 
    # Input Guess Number
    guessN = input("Guess a number: ")
 
    # Use H for HELP command
    if guessN == "H":
        print("Use the following commands:")
        print("[H] (View help commands)")
        print("[N] (View gussed numbers)")
        continue
 
    # Use N for NUMBERS command
    if guessN == "N":
        if len(numbersG) > 0:
            i = 0
            for numberV in numbersG:
                i += 1
                print("%s) %s" % (i, numberV))
        else:
            print("No numbers has been guessed yet.")
        continue
 
    # Adding all number being guessed on list
    numbersG.append(guessN)
 
    # Tracking and storing all numbers
    tries += 1
 
    # Any numbers that are valid and correct
    if int(guessN) == randomN:
 
        print("Correction with number " + str(tries) + " attempts.")
        print("Amount of number you have guessed:")
 
        # Printing out all numbers
        for numberV in numbersG:
            print(numberV)
 
        # Halt while loop from script running
        gameR = False
 
    elif int(guessN) < randomN:
        print("Higher number.")
    else:
        print("Lower number.")
