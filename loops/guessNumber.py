import random

def right_notRight(guess):
    if(guess == random_number):
        print("Got it!!")
    elif(guess < random_number):
        print("Too low!")
    else:
        print("Too high!")


random_number = random.randint(1,21)

guess = int(input("Guess the number: "))

right_notRight(guess)

while(guess != random_number):

    guess = int(input("Guess the number: "))

    right_notRight(guess)

