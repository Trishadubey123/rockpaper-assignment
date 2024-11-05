import random

def explain_rules():
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    return input("Enter rock, paper, or scissors: ").lower()

def determine_winner(player, computer):
    # Added print statements for verification
    print("Determining winner...")  # New line for branch change verification

    while player == computer:
        print("It's a tie! Computer chooses again...")
        computer = get_computer_choice()
        print(f"New computer choice: {computer}")

    if (player == "rock" and computer == "scissors") or \
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

        # Prompt for playing again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

            # Verification line added to ensure changes are detected
print("This is a new line for change verification.")


if __name__ == "__main__":
    main()
