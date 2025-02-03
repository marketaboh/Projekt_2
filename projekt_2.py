"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Markéta Boháčková
email: bohackovama@gmail.com
"""
import random

print("Hi there!")
print("-" * 50)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-" * 50)

def check_input(input):
    if input.isdigit() and len(set(input)) == 4 and input[0] != '0':
        return True
    elif input.isdigit() and input[0] == '0':
        print("Please enter a 4 digit number without leading zeros.")
        return False
    elif input.isdigit() and len(input) != 4:
        print("Please enter a 4 digit number.")
        return False
    elif  input.isdigit() and len(set(input)) != 4:
        print("Please enter a 4 digit number with unique digits.")
        return False
    else:
        print("Please enter a number.")
        return False
    
def generate_unique_digit_number():
    """ function generates a random 4 digit number with unique digits """
    while True:
        number = random.randint(1000, 9999)
        str_number = str(number)
        if len(set(str_number)) == 4:  # Check if all digits are unique
            return number

# generate a random 4 digit number
random_number = generate_unique_digit_number()
print("Random číslo: ",random_number)

# Loop until a valid input is entered
while True:
    user_input = input("Enter a number: ")
    if check_input(user_input):
        break  # Exit the loop if input is valid
print("-" * 50)

print(user_input)
random_number = str(random_number)
attempts = 1
while user_input != random_number:
    bulls = 0
    cows = 0
    attempts += 1
    if user_input != random_number:
        for i in range(4):
            if user_input[i] == random_number[i]:
                bulls += 1
            elif user_input[i] in random_number:
                cows += 1
        print(f"{bulls} bulls, {cows} cows")
        while True: 
            user_input = input("Enter a number: ")
            print("-" * 50)
            if check_input(user_input):
                break
        continue      
    else:
        break
    
print(f"Correct, you've guessed the right number in {attempts} guesses!") 

