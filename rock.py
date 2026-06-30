import random

import time

option = ["rock", "paper", "scissors"]

print("welcome to the rock paper scissors game")
print("choose your option from rock, paper, scissors")


while True:
    user_choice = input("Enter your choice:").lower()


    if user_choice == "quit":
        print("Thanks for playing the game")
        break
    if user_choice not in option:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue




    computer_choice = random.choice(option)
 
    print("Computer choice is:", computer_choice)
    time.sleep(5)


    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("you win! rock beats scissors")
        else:
            print("you lose! paper beats rock")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("computer  win! scissors beats paper")
        else:
            print("you lose! paper beats rock")

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("you win! rock beats scissors")
        else:
            print("you lose! scissors beats paper")
