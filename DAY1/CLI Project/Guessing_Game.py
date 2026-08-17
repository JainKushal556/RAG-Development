# A Number Guessing Game 
# User Will Guess A Number In range(1,50) Its Correct User Win If Wrong We Tell Too High Or Too Low As A Hint

import random
print("..A Number Guessing Game..")
lucky_number = random.randint(1,50)

while True:
    user_guess = int(input("\nEnter Ur Guess(1-50): "))
    if user_guess == lucky_number:
        print("🎉You Win🎉")
        break
    elif user_guess > lucky_number:
        print("!Oops, Too High..")
    elif user_guess < lucky_number:
        print("!Oops, Too Low..")
    else:
        print("...Invalid Number...")

