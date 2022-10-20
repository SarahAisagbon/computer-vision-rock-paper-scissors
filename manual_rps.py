#%%
from ast import Break
import random

#computer randomly selects Rock, Paper or Scissors
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

#user is asked to pick Rock, Paper or Scissors
def get_user_choice():
    user_choice = input("Rock, Paper or Scissors?")
    return user_choice

# Determines who is the winner based on the computer's and the user's choices
def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        winner = "Both"
        
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            winner = "User"
        else:
            winner = "Computer"
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            winner = "User"
        else:
            winner = "Computer"
    else:
        if user_choice == "Rock":
            winner = "User"
        else:
            winner = "Computer"
    
    return winner

#It calls all the functions and runs the game
def play():
    user_wins = 0 
    computer_wins = 0
    
    while user_wins < 3 or computer_wins < 3:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        winner = get_winner(computer_choice, user_choice)
    
        if winner == "Computer":
            computer_wins += 1
        elif winner == "User":
            user_wins += 1
        else:
            user_wins += 1
            computer_wins += 1
    
    if user_wins == 3:
        print("Congratulations! You win")
    elif computer_wins == 3:
        print("Unfortunately, you lost!")
play()
# %%
