#This a full ludo game developed by Godliver and Enoch

#Import random module
import random

#Initialize steps to 0 which counts the number of moves you make
steps = 0

#Global boolean to break loop once a player gets home
isHome= False


#Define a function called dice which returns random numbers from 1-6
def dice():
    return random.randint(1,6)

#Roll allows the user to roll the dice
def roll():
    global steps

    value = dice()
    steps += value
    print("You rolled a ", value)

    print("Move ", value, "steps\n")

    home()
#Alerts player if player has won
def home():
    global isHome
    if steps > 57:
        isHome = True
        print("You won".upper())
    else:
        print("Roll again")



#Main loop controllig the whole game
while True:

    user = input("Ready!\n press r to roll ")
    #Breaking loops if user gets home
    if isHome == True:
        break
    #Allows user to roll dice
    if user == "r":
        roll()

    else:
        print("End game")
        print ("Your total number of steps moved is" ,steps)

        break
