students_scores = {
    "Emma": [85, 90, 78],
    "Liam": [92, 88, 95],
    "Olivia": [70, 75, 80],
    "Noah": [88, 82, 85],
    "Ava": [95, 93, 97]
}

# Print the average score of Olivia
olivia_scores=students_scores["Olivia"]
average=(olivia_scores[0]+olivia_scores[1]+olivia_scores[2])/3
#average=sum(students_scores["Olivia"]) / len(students_scores["Olivia"])
round_avg=round(average,2)
print("The average score of Olivia is: ", round_avg)

# Print the difference of average score of Liam and Olivia
liam_scores=students_scores["Liam"]
liam_average=(liam_scores[0]+liam_scores[1]+liam_scores[2])/3
#average=sum(students_scores["Liam"]) / len(students_scores["Liam"])
round_liam_avg=round(liam_average,2)
print("The average score of Liam is: ", round_liam_avg)
diff=abs(round_liam_avg-round_avg)

print("The difference of average score of Liam and Olivia is: ",diff)

students_scores_2 = {
    "Emma": {"Math": 85, "Science": 90, "English": 78},
    "Liam": {"Math": 92, "Science": 88, "English": 95},
    "Olivia": {"Math": 70, "Science": 75, "English": 80},
    "Noah": {"Math": 88, "Science": 82, "English": 85},
    "Ava": {"Math": 95, "Science": 93, "English": 97}
}

# Update the Score in Math for Emma to 70
students_scores_2["Emma"]["Math"]=70
print(students_scores_2["Emma"])

# Add a subject "Python" for Noah , and provide the score 95 for this subject.
students_scores_2["Noah"]["Python"]=95
print(students_scores_2["Noah"])

# Print the difference of score in Science for Liam and Ava
difference=abs(students_scores_2["Liam"]["Science"]-students_scores_2["Ava"]["Science"])
print("The difference of score in Science for Liam and Ava is: ",difference)

# Add your name to this diocitonary , and feed in your scores for all the subjects.
students_scores_2["Sher"]={}
students_scores_2["Sher"]["Math"]=100
students_scores_2["Sher"]["Science"]=99
students_scores_2["Sher"]["English"]=95

print(list(students_scores_2.keys()))
print(list(students_scores_2.values()))
print(list(students_scores_2.items()))

city_details = {
    "New York": {"Population": 8419000, "Country": "USA"},
    "Los Angeles": {"Population": 3980000, "Country": "USA"},
    "Chicago": {"Population": 2716000, "Country": "USA"},
    "Houston": {"Population": 2328000, "Country": "USA"},
    "Phoenix": {"Population": 1690000, "Country": "USA"}
}

#Q3
# Write a Python program to add a new city, "San Francisco", with a population of 883305 and country "USA" to the city_details dictionary.
city_details["San Francisco"]={}
city_details["San Francisco"]["Population"]=883305
city_details["San Francisco"]["Country"]="USA"

print(list(city_details["San Francisco"].keys()))

# Write a Python program to update the population of "Chicago" to 2800000 in the city_details dictionary.
city_details["Chicago"]["Population"]=2800000
print(list(city_details["Chicago"]))

# Write a Python program to remove the city "Phoenix" from the city_details dictionary.
city_details.pop("Phoenix")
print(list(city_details.keys()))

# Write a Python program to add a new key "Mayor" with the value "Bill de Blasio" to the "New York" dictionary within city_details.
city_details["New York"]["Mayor"]="Bill de Blasio"
print(list(city_details["New York"]))

print(list(city_details.keys()))
print(list(city_details.items()))




