import random

n = random.randint(0, 2)

computer = ""
if n == 0:
    computer = "rock"
elif n == 1:
    computer = "paper"
else:
    computer = "scissor"


def rock():
    if computer == "rock":
        print("Tie")
    elif computer == "paper":
        print("You loose")
    else:
        print("You win")

def paper():
    if computer == "paper":
        print("Tie")
    elif computer == "scissor":
        print("You loose")
    else:
        print("You win")

def scissor():
    if computer == "scissor":
        print("Tie")
    elif computer == "rock":
        print("You loose")
    else:
        print("You win")

choice = input("choose: ").strip().lower()

if choice == "rock":
    rock()
elif choice == "paper":
    paper()
else:
    scissor()