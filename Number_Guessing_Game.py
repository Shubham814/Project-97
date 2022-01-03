import random

numbers = [1,2,3,4,5,6,7,8,9]
number = random.choice(numbers)
chances = 0

print("___Welcome to the Number Guessing Game___")

while chances<5:
    chances+=1
    guess = int(input("Enter a guess for the number (between 1 to 9) : "))
    if guess>number:
        if chances < 5:
            print("Your Guess is larger than the number. Enter a number smaller than" , guess )
            print("                         ")
        else:
            print("___You LOSE! The number is", number)
            print("                 ")
    elif guess<number:
        if chances < 5:
            print("Your Guess is smaller than the number. Enter a number larger than" , guess)
            print("                         ")
        else:
            print("___You LOSE! The number is", number)
            print("                 ")
    else:
        if chances < 5:
            print("___Congratulations! You Got the right number___")
            print("                         ")
            chances = 10
        else:
            print("You LOSE! The number is", number)
            print("                 ")
