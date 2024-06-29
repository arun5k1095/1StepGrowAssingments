
'''Develop a Random Guessing Game using Python programming where a user must guess a randomly
generated number within a defined range. The challenge is to guess the number correctly within a
limited number of attempts.'''

import random

play_again = 'yes'


while play_again.lower() in ('yes','y'):
    count = 0
    answered_correctly = 0
    input_range_start   = int(input("Enter a starting number for range: "))
    input_range_end     = int(input("Enter a ending number for range: "))

    number_to_guess = int(random.randrange(input_range_start, input_range_end))

    print(number_to_guess)

    while count < 5 and answered_correctly == 0:
        guessed_number = int(input("Enter your guess: "))

        if guessed_number == number_to_guess :
            print(f"Congratulations! You guessed the number in {count+1} attempts!")
            answered_correctly = 1
            break
        elif guessed_number < number_to_guess:
            print("Too low, try again.")
        elif guessed_number > number_to_guess:
            print("Too high, try again.")
        count = count + 1

    if answered_correctly == 0:
        print(f"Game over! The correct number was {number_to_guess}.")

    play_again = input("Would you like to play again. Type Yes/No : ")



