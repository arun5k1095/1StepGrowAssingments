

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



# ASSIGNMENT | 11th AUG | DICTIONARY

# Q1
students_scores = {
    "Emma": [85, 90, 78],
    "Liam": [92, 88, 95],
    "Olivia": [70, 75, 80],
    "Noah": [88, 82, 85],
    "Ava": [95, 93, 97]
}
# Print the average score of Olivia
olivia_avg = round((students_scores["Olivia"][0] + students_scores["Olivia"][1] + students_scores["Olivia"][2])/3,2)
print("Average score of Olivia: ", olivia_avg)

# Print the difference of average score of Liam and Olivia
liam_avg = round((students_scores["Liam"][0] + students_scores["Liam"][1] + students_scores["Liam"][2])/3,2)
print("Average score of Liam: ", liam_avg)
print("Difference in average score of Liam and Olivia: ", liam_avg - olivia_avg)

#Q2

students_scores = {
    "Emma": {"Math": 85, "Science": 90, "English": 78},
    "Liam": {"Math": 92, "Science": 88, "English": 95},
    "Olivia": {"Math": 70, "Science": 75, "English": 80},
    "Noah": {"Math": 88, "Science": 82, "English": 85},
    "Ava": {"Math": 95, "Science": 93, "English": 97}
}
# Update the Score in Math for Emma to 70
print("Emma's score in Math before change: ", students_scores["Emma"]["Math"])
students_scores["Emma"]["Math"] = 70
print("Emma's score in Math after change: ", students_scores["Emma"]["Math"])

# Ass a subject "Python" for Noah , and provide the score 95 for this subject.
print("Noah's current scores in all subjects: ", students_scores["Noah"])
students_scores["Noah"]["Python"] = 95
print("Noah's scores after adding Python as new subject: ", students_scores["Noah"])

# Print the difference of score in Science for Liam and Ava
print("Difference in score in Science for Liam and Ava: ", students_scores["Liam"]["Science"] - students_scores["Ava"]["Science"])

# Add your name to this dicitonary , and feed in your scores for all the subjects.
students_scores["Priya"] = {"Math" : 99, "Science" : 96, "English" : 95, "Python" : 97}
print("Added new student 'Priya' in the score list: ", students_scores["Priya"])


#Q3

city_details = {
    "New York": {"Population": 8419000, "Country": "USA"},
    "Los Angeles": {"Population": 3980000, "Country": "USA"},
    "Chicago": {"Population": 2716000, "Country": "USA"},
    "Houston": {"Population": 2328000, "Country": "USA"},
    "Phoenix": {"Population": 1690000, "Country": "USA"}
}

# Write a Python program to add a new city, "San Francisco", with a population of 883305 and country "USA" to the city_details dictionary.
print("City details before change: ", city_details)
city_details["San Francisco"] = {"Population" : 883305, "Country" : "USA"}
print("City details after adding 'San Francisco': ", city_details)

# Write a Python program to update the population of "Chicago" to 2800000 in the city_details dictionary.
print("Chicago population before change: ", city_details["Chicago"]["Population"])
city_details["Chicago"]["Population"] = 2800000
print("Chicago population after change: ", city_details["Chicago"]["Population"])

# Write a Python program to remove the city "Phoenix" from the city_details dictionary.
print("City details before removing Phoenix: ", city_details)
del city_details["Phoenix"]
print("City details after removing Phoenix: ", city_details)

# Write a Python program to add a new key "Mayor" with the value "Bill de Blasio" to the "New York" dictionary within city_details.
print("New York city details before change: ", city_details["New York"])
city_details["New York"]["Mayor"] = "Bill de Blasio"
print("New York city details after change: ", city_details["New York"])


#Q4
movie_details = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Release_Year": 2010,
    "Genres": ["Action", "Sci-Fi", "Thriller"],
    "Cast": {
        "Leonardo DiCaprio": "Cobb",
        "Joseph Gordon-Levitt": "Arthur",
        "Elliot Page": "Ariadne",
        "Tom Hardy": "Eames"
    },
    "Duration_Minutes": 148,
    "Rating": 8.8,
    "Box_Office_Millions": 829.89
}
# Update the rating to 9.0.
print("Movie Rating before change: ", movie_details["Rating"])
movie_details["Rating"] = 9.0
print("Movie Rating after change: ", movie_details["Rating"])

#Add a new key-value pair for "Budget" with a value of 3 160 million.
movie_details["Budget"] = 3160000000
print("Movie Budget added :", movie_details["Budget"])

# Insert a new cast member into the nested dictionary.
movie_details["Cast"]["Tom Hanks"] = "Johnny"
print("New cast added: ", movie_details["Cast"])

#Remove the "Box_Office_Millions" entry.
print("Movie Box_Office_Millions details: ", movie_details["Box_Office_Millions"])
del movie_details["Box_Office_Millions"]
print("Movie details after removing Box_Office_Millions: ", movie_details)

#Add "Mystery" to the genres list.
movie_details["Genres"].append("Mystery")
print("Movie details after adding in Genres:", movie_details["Genres"])

#Remove "Sci-Fi" from the genres list.
print("Movie Genres before change: ", movie_details["Genres"])
movie_details["Genres"].remove("Sci-Fi")
print("Movie Genres after change: ", movie_details["Genres"])



