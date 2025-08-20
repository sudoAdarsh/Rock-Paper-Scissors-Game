import random

computer = random.choice(["rock", "paper", "scissor"])

choice = input("choose: ").strip().lower()

if choice == computer:
    print("Tie")
elif (choice, computer) in [("rock", "scissor"), ("paper", "rock"), ("scissor", "paper")]:
    print("You win")
else:
    print("You loose")
