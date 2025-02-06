
rps = input("Rock","Paper","Scissors")
from random import *
selections = ["Rock","Paper","Scissors"]
computerChoice = selections[randint(0,2)]
userChoice = input("Choose rock, paper or scissors")

if (choice == "paper") and  (choice == "scissors"):
    print = ("Well done user_1")
computerChoice = int(input("Rock and paper: "))
if def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock"and computer_choice == '"scissors") or 
         (user_choice == "scissors" and computer_choice == "paper") or 
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
