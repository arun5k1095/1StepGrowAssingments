

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

#"""
# Ask user to provide email id and fetch domain from it
email = input("Please enter your email address: ")
print(email.split("@")[-1].split(".")[0])
#"""

# ASSIGNMENT 3 | LISTS

# Given the list sports = ['Cricket', 'Football', 'Basketball', 'Tennis', 'Hockey'], how would you access the first two and last elements of the list?
sports = ["Cricket", "Football", "Basketball", "Tennis", "Hockey"]
output1 = sports[:2]
output1.append(sports[-1])
print("Displaying first 2 and last sport in the list: ", output1)

# Using the sports list, how would you create a new list containing the first three sports?
output2 = sports[:3]
print("Displaying first 3 sports in the list: ", output2)

# How would you add the sport 'Badminton' to the sports list?
sports.append("Badminton")
print("Adding Badminton to the list of sports: ", sports)

# How would you insert the sport 'Swimming' at the third position in the sports list?
sports.insert(2,"Swimming")
print("Added Swimming in 3rd position in sports list: ", sports)

# If you want to remove 'Tennis' from the sports list, which method would you use, and how would you write it?
sports.remove("Tennis")
print("Removed Tennis from the sports list: ", sports)

# How would you reverse the order of elements in the sports list?
sports.reverse()
print("Reversed sports list: ", sports)

# How would you find the index of 'Basketball' in the sports list?
print("Position of 'Basketball' in the sports list: ", sports.index("Basketball"))

# If the sports list had multiple occurrences of 'Football', how would you count how many times 'Football' appears in the list?
sports.append('Football')
print("Number of times 'Football' is present in the sports list: ", sports.count("Football"))

# How would you combine the sports list with another list called outdoor_games = ['Golf', 'Rugby']?
outdoor_games = ['Golf', 'Rugby']
sports = sports + outdoor_games
print("Combined sports and outdoor games as a single list: ", sports)




