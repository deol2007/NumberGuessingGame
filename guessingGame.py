import random

while chances < 5:
    number=random.randint(1,10)
    guess=input("Guess a Number Between 1 and 10:")
    chances = chances + 1
if guess > number:
    guess=input("Too High, guess a lower number:")

if guess < number:
    guess=input("Too Low, guess a higher number:")

if guess = number:
    print("You guessed the number!")

if not chances <5:
    print("You didn't guess the number, the number is:", number)