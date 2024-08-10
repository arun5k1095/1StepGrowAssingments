#Assignment 1
# Ask user to enter scores in 3 subjects, calculate the average, and print the results

print("Please enter your scores in following subjects")
Math = float(input("Maths: "))
Science = float(input("Science: "))
English = float(input("English: "))
AverageMarks= (Math+Science+English)/3
print("Your average marks is: ", round(AverageMarks,2))


#Assignment 2
# Write a Python program that takes the principal amount, rate of interest, and time from the user and calculates the simple interest. And print the result.

principal = float(input("What is the deposit amount(Rs): "))
rate_of_interest = float(input("What is the rate if interest(%): "))
duration = float(input("What is the deposit duration(yrs): "))
SI = (principal * rate_of_interest * duration)/100

print("Simple Interest accrued for the deposit terms mentioned is: Rs ", round(SI,2))
