# import random number generator
import random
import time

# variables:
tries = 0
name = ''
number = random.randint(0,101)
found = False

# intro
print("in this game you will have to guess a number in the least number of tries.")
time.sleep(1)
print("First, I would like to know your name.")
time.sleep(.5)
print("What's yor name?")
name = input()
print("Thank you", name ,".I have selected a number between 0 and 100, try to guess it!")

# game loop
while found == False:
    tries +=1
    print("What is your guess number ",tries,"?")
    guess = input()

    #casting the input as an int
    guess = int(guess)

    if guess < number:
        print("Your number is lower than mine, try again")

    if guess > number:
        print("Your number is higher than mine, try again")

    if guess == number:
        found = True
        break

# ending
print("Congratulations! You found my number in",tries,"tries")