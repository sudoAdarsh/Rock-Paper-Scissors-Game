# Author : Adarsh Upadhyay 

import random

# ASCII art definitions
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

# Dictionary for easy lookup
ascii_art = {
    "rock": Rock,
    "paper": Paper,
    "scissor": Scissor
}

# Score Tally
wins = 0
losses = 0
ties = 0

while True:
    choice = input("\nChoose Rock, Paper, Scissor (or type 'quit' to exit): ").strip().lower()

    # Quit condition
    if choice == "quit":
        print("Thanks for playing!")
        print(f"\nFinal Score → Wins: {wins}, Losses: {losses}, Ties: {ties}")
        break

    # Invalid input check
    if choice not in ascii_art:
        print("Invalid choice. Please type rock, paper, or scissor.")
        continue

    # Computer's choice
    computer = random.choice(["rock", "paper", "scissor"])

    # Show choices with ASCII art
    print(f"\nYou chose {choice}:")
    print(ascii_art[choice])

    print(f"Computer chose {computer}:")
    print(ascii_art[computer])

    # Updating ScoreBoard and deciding Results
    if choice == computer:
        print("Result: Tie")
        ties += 1
    elif (choice, computer) in [("rock", "scissor"), ("paper", "rock"), ("scissor", "paper")]:
        print("Result: You win!")
        wins += 1
    else:
        print("Result: You lose!")
        losses += 1

    # Show ScoreBoard
    print(f"Score → Wins: {wins}, Losses: {losses}, Ties: {ties}")
