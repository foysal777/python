import random

secret_number = random.randint(1,20)
attempts = 0
print("welcome to the number of guessing game")

while True:
    guess = int(input("Enter your guess between 1 to 20:"))
    attempts = attempts + 1
    print("your guess is:", guess)
    if guess == secret_number:
        print("congratulations! your guess is correct", guess)
        print("you took", attempts, "number of time")
        break
    elif guess > secret_number:
        print("choose a smaller number")
    elif guess < secret_number:
        print( "choose a bigger number")
        