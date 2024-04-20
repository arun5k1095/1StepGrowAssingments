import random as rd

user_input = "Y"

while user_input == "Y" :
    top_limit = int(input("please enter the top limit of the number range: "))
    bottom_limit = int(input("please enter the bottom limit of the number range: "))
    random_number = rd.randrange(bottom_limit, top_limit, 1)
    print(random_number)
    counter = 0
    while counter < 5 :
        user_input_num = float(input(f"Please enter guess numeber {counter+1}: "))
        if user_input_num > random_number :
            print("Too high,Try again")
        elif user_input_num < random_number :
            print("Too low,Try again")
        elif user_input_num == random_number :
            print(f"congratulations! you guessed the correct number in {counter+1} attempts")
            break
        counter = counter + 1

    if counter >= 5:
        print(f"Game Over!The correct number was {random_number}")
    user_input = input("Do you want to play again?(Y/N)").upper()
    if user_input == "Y":
        continue
    elif user_input == "N":
        break
    while user_input not in ["Y","N"]:
        print("wrong input")
        user_input = input("Do you want to play again?(Y/N)").upper()


