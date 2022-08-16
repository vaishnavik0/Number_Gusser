# Number Gusser
# In this we are going to generate a random number and we will track how much time it takes the user to guess the number


# Python Random module is an in-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these are not truly random. This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc.
import random


# int(25) --> 25 digit if we put int("Hello") --> error
# random number generation 
top_of_range = input("Type a number: ")


# isdigit will return us true if this is a number types by the user 
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()

else:
    print('please type a number next time. ')
    quit()

random_number = random.randint(0,top_of_range) #randint(-5,11) it will include number 11

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('please type a number next time. ')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    
    elif user_guess > random_number :
        print("you were above the number!")
    else:
        print("you were below the number!")
       

print('You got it in' , guesses , "guesses")