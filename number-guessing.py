#Number guessing game  

import random

print("Welcome to the Number Guessing Game\nCreated by Stark")
min_num = int(input("Enter Lower Bound:"))
max_num = int(input("Enter Upper Bound: "))
print("You have only 8 tries")
num = random.randint(min_num, max_num)


i = 0
while i < 8:
    user_input = int(input("Guess a number: "))
    i += 1
    if i == 8:
        print("You fail :( \nThe number is",num  )
        break
    if user_input > num:
        print(f"Too High \nTry again, Remaining tries {8-i}")
    elif user_input < num:
        print(f"Too low \nTry again, Remaining tries {8-i}")
    elif user_input == num:
        print(f"You Won :)")
        break
    else:
        print("Invalid input")

        