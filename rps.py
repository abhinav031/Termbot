# Rock Papaer Scissors

# Imports
from random import randint


def rps():
    t = ["Rock", "Paper", "Scissors"]

    computer = t[randint(0, 2)]

    player = False

    while player == False:

        player = input("Rock, Paper, Scissors? ")
        if player == computer:
            print("Tie!")
        elif player.capitalize() == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player.capitalize() == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player.capitalize() == "Scissors" or "Scissor":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        elif player.capitalize() == "Exit":
            exit()
        else:
            print("That's not a valid play. Check your spelling!")

        player = False
        computer = t[randint(0, 2)]
