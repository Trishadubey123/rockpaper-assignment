cd rockpaper-assignment
import random

import random

def explain_rules():
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    return input("Enter rock, paper, or scissors: ").lower()

def determine_winner(player, computer):
    while player == computer:
        print("It's a tie! Computer chooses again...")
        computer = get_computer_choice()  # Generate a new computer choice
        print(f"New computer choice: {computer}")

    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

        return "Computer wins!"

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    return input("Enter rock, paper, or scissors: ").lower()

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
# This is a test change to ensure commits are reflected
print("This is a test change in the Noties branch")

# This is a new change to verify the new branch
print("This change is to verify that the new-noties-branch has distinct changes")

print("new branch")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    explain_rules()
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        if result != "It's a tie!":
            break  # End the game if there's a winner

if __name__ == "__main__":
    main()
