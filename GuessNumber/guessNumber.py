# This a very simple game developed in Python.
# The program generates a random integer between 0 and 100.
# The user is trying to guess it. The program helps the user to find
# the hidden number by giving him hints and terminates only when he
# finds the correct number or he reaches the maximum number of attempts.

import random

hidden_number = random.randint(0, 100)
attempts = 0
max_guesses = 5
active = True

while active:
    guess = int(input("Give a number between 0 and 100: "))
    while guess < 0 or guess > 100:
        guess = int(input("Give a number between 0 and 100: "))

    attempts += 1
    if attempts == max_guesses and guess != hidden_number:
        print("You Lose. You reached limit of attempts. The hidden number was: " + str(hidden_number))
        break
    if guess == hidden_number:
        active = False
        print("Congratulations, you have made the right guess of the number: " + str(hidden_number))
    elif guess > hidden_number:
        print("The number is lower than your guess. Please try again!")
    else:
        print("The number is greater than your guess. Please try again!")
    print("You have " + str(max_guesses - attempts) + " attempts left.")
