# Ask user for his/her score in three subjects, calculate the average print the result

Maths = int(input("Score in Maths: "))
English = int(input("Score in English: "))
Science = int(input("Score in Science: "))
Average = (Maths+English+Science)/3
print("Average Score is:", Average)

# Assignment 2 - Write a Python program that takes the principal amount, rate of interest
# and time from the user and calculates the simple interest. And print the result.

Principal = float(input("Enter principal Amount: "))
Rate_of_Interest = float(input("Enter Interest Rate: "))
Tenor = int(input("Enter Tenor: "))
Interest_Amount = (Principal*Rate_of_Interest*Tenor)/100
print("Simple interest is:", Interest_Amount)

# Assignment 3 - Ask user to give a long sentence, convert into upper case and print

Statement = str(input("Please enter a long sentence: "))
Revised_Statement = Statement.upper()
print(Revised_Statement)

# Assignment 4 - Ask user to enter full name, reverse it and print

Statement = str(input("Please provide your full name: "))
Revised_Statement = Statement[::-1]
print(Revised_Statement)

