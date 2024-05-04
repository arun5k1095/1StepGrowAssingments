import random


def guess_game(user_in):
    global computer_guess

    if user_in > computer_guess:
        print("Too high, try again.")

    elif user_in < computer_guess:
        print("Too low, try again.")

    else:
        return True


play_in = "yes"
count = 0

while play_in == "yes":

    computer_guess = random.randint(1, 100)

    flag = False

    while count < 5:

        user_in = int(input("Enter a number between 1 to 100: "))
        out_put = guess_game(user_in)

        if out_put == True:
            print(f"Congratulations! You guessed the number in {count + 1} attempts!")
            pl_again1 = input("Would you like to play again?").lower()

            if pl_again1 == "yes":
                play_in = "yes"
                computer_guess = random.randint(1, 100)
                count = -1
            else:
                flag = True
                break
        count = count + 1

    if flag == True:
        break

    else:
        pl_again = input(f"Game over! The correct number was {computer_guess}. Would you like to play again?").lower()
        if pl_again == "yes":
            play_in = "yes"
            count = 0

        else:
            break

