#!/usr/bin/python
import random

# While loop syntax
# while expression:
#   statement(s)
# You can use else block with while as well
# while expression:
#   statement(s)
# else:
#   statement(s)

guess_num_range = 20
num_to_be_guessed = int(guess_num_range * random.random()) + 1
guess = 0

while guess != num_to_be_guessed:
    guess = int(input("Guess the number: "))
    if guess > 0:
        if guess > num_to_be_guessed:
            print("Number is too large")
        elif guess < num_to_be_guessed:
            print("Number is too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")
