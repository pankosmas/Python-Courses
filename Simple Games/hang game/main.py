# This is hangman game. User tries to guess letters in a random generated hidden word from a list.
# The program examines random, lists, string methods, input check and format print.

from random import randrange

words = ["soccer", "scorer", "football", "player", "coach", "stadium", "pitch", "court", "lights", "referee"]

hidden_word = words[randrange(len(words))]
# hidden_word = random.choice(words)
guessed_letters = []
max_turns = 10

for turn in range(max_turns):

    print(f"TURN{turn + 1}")

    while True:

        letter = input("Make a guess: ").lower()

        if len(letter) != 1:
            print("Give only one letter please.")
        elif not letter.isalpha():
            print("Give a letter please.")
        elif letter in guessed_letters:
            print("You have already given this letter.")
        else:
            break

    guessed_letters.append(letter)
    print(f"{letter} appears {hidden_word.count(letter)} times in hidden word.")

    found = True
    for char in hidden_word:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
            found = False
    print("\n")

    if found:
        print("Success!")
        break
else:
    print("You have reached maximum rounds! You Lose!")
    print(f"The hidden word was {hidden_word}")
