"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Markéta Boháčková
email: bohackovama@gmail.com
"""
import random

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-----------------------------------------------")

def check_is_number(input):
    if input.isdigit() and len(set(input)) == 4 and input[0] != '0':
        return input
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
    
# generate a random 4 digit number
number = random.randint(1000, 9999)
print(number)

# Loop until a valid input is entered
while True:
    user_input = input("Enter a number: ")
    if check_is_number(user_input):
        break  # Exit the loop if input is valid


print(user_input)
#user_input = int(input)

print("-----------------------------------------------")
