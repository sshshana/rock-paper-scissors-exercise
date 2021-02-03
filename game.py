# game.py

print("Rock, Paper, Scissors, Shoot!")



print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
    print("You chose:", user_choice)

else:
    print("You entered:", user_choice, ". Please enter a valid input!")
    exit()


# simulating a computer input

import random

arr = ["rock", "paper", "scissors"]

random.shuffle(arr)
arr

computer_choice = random.choice(arr)

print(f"The computer chose: {computer_choice}")

# determining who won

if user_choice == "rock":
    if computer_choice == "rock":
        print("You ")


print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")