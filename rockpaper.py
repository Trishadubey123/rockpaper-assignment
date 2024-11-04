import random

import random

def explain_rules():
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

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
