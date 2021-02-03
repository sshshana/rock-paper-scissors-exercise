# game.py

print("Rock, Paper, Scissors, Shoot!")



print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
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
    print("Yay, you won! Congratulations.")
elif user_choice == computer_choice:
    print("It's a tie!")
else:
    print("Oh, the computer won.")

print("-------------------")
print("Thanks for playing. Please play again!")