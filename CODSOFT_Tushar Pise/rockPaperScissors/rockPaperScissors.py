import random

user_choice = input("Enter rock, paper, or scissors: ")

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == "rock" and computer_choice == "scissors":
    print("You Win!")

elif user_choice == "paper" and computer_choice == "rock":
    print("You Win!")

elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win!")

else:
    print("Computer Wins!")