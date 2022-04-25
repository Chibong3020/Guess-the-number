import random
import time

number = random.randint(1, 20)
guess = int(input("Guess a number between 1 and 20: "))

while guess != number:
    if guess > number:
        guess = int(input("Too big, try again: "))
    elif guess < number:
        guess = int(input("Too small, try again: "))

if guess == number:
    print (f"Your guess was correct. It was {number}")
    time.sleep(3)
