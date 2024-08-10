#Assignment 1
# Ask user to enter scores in 3 subjects, calculate the average, and print the results

print("Please enter your scores in following subjects")
Math = float(input("Maths: "))
Science = float(input("Science: "))
English = float(input("English: "))
AverageMarks= (Math+Science+English)/3
print("Your average marks is: ", round(AverageMarks,2))