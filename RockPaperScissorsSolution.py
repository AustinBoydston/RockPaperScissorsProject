# Author: Austin Boydston
# Date: 2/18/2024
# Instructor: Austin Boydston
# Description: This program is my solution for a rock paper scissors project assigned to my students. It works by getting a random number from a random number function,
# Then getting input from the user. If the user gives bad input the program exits with an error message. The program maps the users input to an integer value, then compares
# This integer to the computers integer. Depending on the choice, the program prints out who the winner is.


import random

# Get the input from the computer and then from the user.
ComputerChoice = random.randint(1, 3)
print("=====Rock, Paper, Scissors=====")
print("Enter the word \"Rock\", \"Paper\", or \"Scissors\" to play.")
PlayerResponse = input()
PlayerInt = 0

# Map the word given by the human player to an integer value
match PlayerResponse:
    case "Rock":
        PlayerInt = 3
    case "rock":
        PlayerInt = 3
    case "Paper":
        PlayerInt = 2
    case "paper":
        PlayerInt = 2
    case "Scissors":
        PlayerInt = 1
    case "scissors":
        PlayerInt = 1
    case _:
        print("ERROR: Invalid Input") 
        exit()

# map the computer choice to a game choice and print it out to inform the user what the computer chose.
match ComputerChoice:
    case 1:
        print("Computer Chooses Scissors")
    case 2:
        print("Computer Chooses Paper")
    case 3:
        print("Computer Chooses Rock")


# Compare the mapped integer choice of the player with the integer choice of the computer and print the results of the game.
if(PlayerInt == ComputerChoice):
    print("Result: Tie")
elif(PlayerInt == ComputerChoice + 1):
    print("Result: Computer Win")
elif(PlayerInt == ComputerChoice - 1):
    print("Result: Player Win")
elif(PlayerInt == ComputerChoice + 2):
    print("Result: Player Win")
elif(PlayerInt == ComputerChoice - 2):
    print("Result: Computer Win")
    