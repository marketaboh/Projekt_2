"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Markéta Boháčková
email: bohackovama@gmail.com
"""
import random
import time

def check_input(input: str) -> bool:
    """ function checks if the input is a 4 digit number with unique digits 
    and returns True if the input is valid, otherwise returns False 
    and prints an error message 
    input: str ->bool """

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

def play_bulls_and_cows():
    """ function plays a bulls and cows game.
    The player has to guess a 4 digit number with unique digits. 
    The game provides feedback in the form of bulls and cows."""

    print("Hi there!")
    print("-" * 50)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 50)
    random_number = generate_unique_digit_number() # Generate a random 4 digit number
    random_number = str(random_number)
    attempts = 1 # Number of guesses

    # Loop until a valid input is entered 
    while True:
        user_input = input("Enter a number: ")
        start_time = time.time()  # Record the start time
        if check_input(user_input):
            break  # Exit the loop if input is valid
    print("-" * 50)
    
    while user_input != random_number:
        bulls = 0
        cows = 0
        attempts += 1
        for i in range(4):
            if user_input[i] == random_number[i]:
                bulls += 1
            elif user_input[i] in random_number:
                cows += 1
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        while True: 
            user_input = input("Enter a number: ")
            print("-" * 50)
            if check_input(user_input):
                break
        continue      
    end_time = time.time()  # Record the end time
    elapsed_time = int(end_time - start_time)  # Calculate the elapsed time
    print(f"Correct, you've guessed the right number in {attempts} guess{'es' if attempts != 1 else ''}!")
    print(f"It took you {elapsed_time} seconds.")
    print("-" * 50)
    print("That's amazing!")

if __name__ == "__main__":
    play_bulls_and_cows()