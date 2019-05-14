# Import module and the Die Class.
import random
from dice import Die



# Instansiates (creats) new objects from the Die Class.
# These will be our three new dice (Red, Green and Blue dice).
red_die = Die("Red", [0, 0, 4, 4, 8, 8], [])
green_die = Die("Green", [2, 2, 3, 3, 7, 7], [])
blue_die = Die("Blue", [1, 1, 5, 5, 6, 6], [])

# A string variable for calling the winner.
the_winner = "Wait what, no winner??"

# Input from user;
numberofdice = int(input("Choose number of players(2 or 3): "))
numberofrolls = int(input("Choose number of rolls: "))



# Defines a function for using 2 color dice.
def roll_die_2():
    i = 0
    num = numberofrolls
    # Setting variables to global, so we can reuse them outside the function.
    global first_player, second_player


    # Sets the color for the first player.
    if(choose_player1.lower() == "red"): # lower(); convert to lowercase.
        first_player = red_die
    elif(choose_player1.lower() == "green"):
        first_player = green_die
    elif(choose_player1.lower() == "blue"):
        first_player = blue_die
    else:
        print("Something went wrong") # Error message.

    # Sets the color for the second player,
    # and checks if it's not the same as the first player.
    if(choose_player2.lower() == "red" and choose_player1.lower() != "red"):
        second_player = red_die
    elif(choose_player2.lower() == "green" and choose_player1.lower() != "green"):
        second_player = green_die
    elif(choose_player2.lower() == "blue" and choose_player1.lower() != "blue"):
        second_player = blue_die
    else:
        print("You need to choose a different color than player 1!") # Error message.


    # The amount of rolls is decided by the user, when the program is running.
    while i < num:
        roll1 = random.choices(first_player.getSides())[0]
        roll2 = random.choices(second_player.getSides())[0]

        if(roll1 > roll2):
            first_player.getScores().append("+")
        else:
            second_player.getScores().append("+")
        i = i + 1


# Defines a function for using all 3 color dice.
def roll_die_3():
    i = 0
    num = numberofrolls


    # The amount of rolls is decided by the user, when the program is running.
    while i < num:
        roll1 = random.choices(red_die.getSides())[0]
        roll2 = random.choices(green_die.getSides())[0]
        roll3 = random.choices(blue_die.getSides())[0]

        if(roll1 > roll2 and roll1 > roll3):
            red_die.getScores().append("+")
        elif(roll2 > roll1 and roll2 > roll3):
            green_die.getScores().append("+")
        elif(roll3 > roll1 and roll3 > roll2):
            blue_die.getScores().append("+")
        i = i + 1



# Chosing which function to run and what to print from the results,
# based on how many users that are playing (2 or 3) the game.
if(numberofdice == 2): # Two players.
    choose_player1 = input("Choose which color die " +
                           "you want [Red, Green, Blue]: ")
    # Calling (using) the Die toString() method. 
    if(choose_player1.lower() == "red"):
        print(red_die.toString())
    elif(choose_player1.lower() == "green"):
        print(green_die.toString())
    elif(choose_player1.lower() == "blue"):
        print(blue_die.toString())
    else:
        print("You must chose one of the 3 colors!") # Error message.

    choose_player2 = input("Choose which color die " +
                           "you want [Red, Green, Blue]: ")
    # Calling (using) the Die toString() method. 
    if(choose_player2.lower() == "red"):
        print(red_die.toString())
    elif(choose_player2.lower() == "green"):
        print(green_die.toString())
    elif(choose_player2.lower() == "blue"):
        print(blue_die.toString())
    else:
        print("You must chose one of the 3 colors!") # Error message.

    # Calling (using) the right function,
    # based on numbers of players.
    roll_die_2()


    # Checking for the right winner and returns the winner of the game.
    if(len(first_player.getScores()) > len(second_player.getScores())):
        the_winner = first_player.getColor() + " is the winner!"
    else:
        the_winner = second_player.getColor() + " is the winner!"

    print(str(first_player.getColor()) + " : " +
          str(len(first_player.getScores())))
    print(str(second_player.getColor()) + " : " +
          str(len(second_player.getScores())))
    print(the_winner)


elif(numberofdice == 3): # Three players.
    # Calling (using) the right function,
    # based on numbers of players.
    roll_die_3()

    # Checking for the right winner and returns the winner of the game.
    if(len(red_die.getScores()) > len(green_die.getScores()) and
       len(red_die.getScores()) > len(blue_die.getScores())):
        the_winner = red_die.getColor() + " is the winner!"
    elif(len(green_die.getScores()) > len(red_die.getScores()) and
         len(green_die.getScores()) > len(blue_die.getScores())):
        the_winner = green_die.getColor() + " is the winner!"
    elif(len(blue_die.getScores()) > len(red_die.getScores()) and
         len(blue_die.getScores()) > len(green_die.getScores())):
        the_winner = blue_die.getColor() + " is the winner!"
    else:
        the_winner = "Something went very wrong here!" # Error message.

    print(red_die.toString())
    print(green_die.toString())
    print(blue_die.toString())
    print(str(red_die.getColor()) + " : " + str(len(red_die.getScores())))
    print(str(green_die.getColor()) + " : " + str(len(green_die.getScores())))
    print(str(blue_die.getColor()) + " : " + str(len(blue_die.getScores())))
    print(the_winner)

else:
    print("Game doesn't work with " + str(numberofdice) + " dice") # Error message.
