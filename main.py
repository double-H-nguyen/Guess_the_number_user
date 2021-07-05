# Requirements
# * User will select their own number
# * Computer will try to guess the number
import random


def main():
    # Ask user to input a number between 1-10
    user_num = int(input('Input a number between 1-10: '))

    # Computer will start in the middle
    comp_guess = 5

    while True:
        # If computer's guess is greater than user's input, then decrement the computer next guess
        if comp_guess > user_num:
            print(f'Computer guessed {comp_guess} and was too high')
            comp_guess -= 1
        # If computer's guess is less than user's input, then increment the computer next guess
        elif comp_guess < user_num:
            print(f'Computer guessed {comp_guess} and was too low')
            comp_guess += 1
        # If computer's guess equals user's input, then stop the program
        elif comp_guess == user_num:
            print(f'Computer guessed {comp_guess} and was correct!')
            break


# Computer will randomly guess
def comp_rand_guess():
    # Ask user to input a number between 1-100
    user_num = int(input('Input a number between 1-100: '))

    low = 1
    high = 100

    while True:
        # computer guess a number
        comp_guess = random.randint(low, high)
        print(f'Computer guessed {comp_guess}')
        # if guess is higher than user's input, then use guess number as new high
        if comp_guess > user_num:
            high = comp_guess - 1
        # if guess is less than user's input, then use guess number as new low
        elif comp_guess < user_num:
            low = comp_guess + 1
        # if guess is equal to user's input, then exit the program
        elif comp_guess == user_num:
            print(f'Computer guess was correct!')
            break


if __name__ == '__main__':
    # main()
    comp_rand_guess()
