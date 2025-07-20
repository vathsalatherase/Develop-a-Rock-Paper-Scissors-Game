import random

# Allowed choices
choices = {"rock", "paper", "scissors"}

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = input("Enter your move (rock, paper, or scissors): ").lower()

        if user_choice not in choices:
            print("Invalid input. Please try again.")
            continue

        computer_choice = random.choice(list(choices))
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

# Run the game
play_game()
