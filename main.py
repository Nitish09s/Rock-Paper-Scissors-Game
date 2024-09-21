import random

def get_computer_choice():
    """Return a random choice for the computer: 'rock', 'paper', or 'scissors'."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Get the user's choice and validate the input."""
    while True:
        user_input = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the rules of Rock-Paper-Scissors."""
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"

    return "You lose!"

def play_again():
    """Ask the user if they want to play again."""
    while True:
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay in ['yes', 'no']:
            return replay == 'yes'
        else:
            print("Please answer with 'yes' or 'no'.")

def play_game():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Show choices
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
