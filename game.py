# game.py

# Import all the modules and third-party packages that contain the functionality we need:
# We want to allow users choose their own user names by creating a separate virtual environment

import os
import random

from dotenv import load_dotenv 

# After that, we generally run any setup code, like setting environment vars:

load_dotenv() # this one happens to read env vars from the ".env" file (read README.md)

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable


print("Rock, Paper, Scissors, Shoot!")

print("-------------------")
print(f"Welcome '{PLAYER_NAME}' to my Rock Paper Scissors game...")
print("-------------------")

#asking user for an input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")


#validate the user selection

rbs = ["rock", "paper", "scissors"]

if user_choice in rbs:
    print("You chose:", user_choice)

else:
    print("Please choose a valid option and try again.")
    exit()

# simulating a computer input

import random

computer_choice = random.choice(rbs)

print(f"The computer chose: {computer_choice}")


print("-------------------")

# determining who won

result = (user_choice, computer_choice)
wins = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]

if result in wins:
    print(f"Yay, you won! Congratulations, {PLAYER_NAME}.")
elif user_choice == computer_choice:
    print("It's a tie!")
else:
    print("Oh, the computer won. That's ok.")

print("-------------------")
print("Thanks for playing. Please play again!")