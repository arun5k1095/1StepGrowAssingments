"""
print("Welcome to the program!")

author = "Sherry"
age = 15


def myfunc():
    print("I am inside the function")
    print("Time to go back!")
    print("Now I am the end of the function")


myfunc()
print("Thank you!")

myfunc()
print("The end.")


def addition(num1, num2):
    result = num1 + num2
    print(result)


addition(50, 100)
addition(80, 200)


def addup(data):
    total = 0

    for number in data:
        print(number, end=" ")
        # print(number, end="---")
        total = total + number

    print(total)

addup([5,1,15,20])
addup([80,90,56,45,20,13,80])

"""

# Create a function that prints all even numbers between two given numbers (inclusive).

"""
def print_even(num1, num2):
    even_numbers = []
    for i in range(num1, num2+1):
        if i % 2 == 0:
            even_numbers.append(i)

    print(even_numbers)
    
    # while num1 <= num2:
    #     if num1 % 2 == 0:
    #         print("Even number found: ", num1)
    #     
    #     num1 = num1 + 1
        
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print_even(num1, num2)

"""

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def AddupNumbers(curr_num, final_num):
    numbers = []
    while curr_num <= final_num:
        numbers.append(curr_num)
        curr_num = curr_num+1

    total = sum(numbers)

    return total ,500  #will store it as a tuple

response, status = AddupNumbers(num1, num2)
print(response)
print(status)

"""
"""
def Addition(num1, num2, operator):
    return num1 + num2

def Subtraction(num1, num2, operator):
    return num1 - num2

def Multiplication(num1, num2, operator):
    return num1 * num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter your operator (+,-,*): ")
# if operator not in "+-/":
    print("Enter a valid operator")
    exit()

if operator == "+":
    print("The sum of numbers is: ", Addition(num1,num2,operator))

elif operator == "-":
    print("The difference of numbers is: ", Subtraction(num1,num2,operator))

elif operator == "*":
    print("The product of numbers is: ", Multiplication(num1,num2,operator))

else:
    print("Incorrect operator added!")
    
"""

"""
def compute(num1, num2, operator):
    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."

        return num1 / num2

    else:
        return "Incorrect Operator added."

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter your operator (+,-,*): ")
response = compute(num1, num2, operator)
print("The answer is: ", response)

"""

#Local scope and global scope

# score=600
#
# def myfunc():
#     score=200
#     print(score)
#
# print(1, score)
# myfunc()
# print(1, score)


# score = 600
#
# def myfunc():
#     global score
#     score = 200
#     print(score)
#
# print(1, score)
# myfunc()
# print(1, score)

# Default value in arguments
# def myfunc(x=10, y=20, z=30):
#     total = x + y + z
#
#     print(total)
#
# myfunc(5, 10)
# myfunc(x=5, z=40)

def Addup(*data):
    print(data)

Addup(3, 4, "Don", "Sherry", [1,2,3,4],{"name": "Sherry"})

def Addup(**data):
    print(data)

Addup(name="Sherry", age=[1,2,3,4], see={"name": "Sherry"}, country="Pakistan")