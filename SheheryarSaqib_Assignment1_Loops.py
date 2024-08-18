
"""
count=0

while count<5:
    # print("Sherry")
    num1 = input("Enter your score 1:")
    num2 = input("Enter your score 2:")
    result = num1 + num2
    print("The total sum is :", result)
    count = count + 1

# Ask user for a number. Print all the numbers until that number using while loop.
current_num=0
number=int(input("Please enter a number: "))

while(current_num<number):
    print(current_num)
    current_num=current_num+1

# Ask user for a number  , starting this numbers , all the way upto 0 , orint all the numbers in reverse order.
number=int(input("Please enter a number: "))
current_num=number

while(current_num>=0):
    print(current_num)
    current_num=current_num-1

# Ask user for  number , and starting from 0 all way to this number , you must add up all the numbers
# and print the result

result=0
input_number=int(input("Please enter a number: "))
current_num=0

while (current_num<=input_number):
    result=result+current_num
    current_num=current_num+1

print("The sum to that number is: ",result)

# Create a program that continuously asks the user to input a number and then prints the square of that number.
# The program should keep running until the user inputs a negative number.
# Once a negative number is entered, the program should stop.

num=999
while(num>=0):
    num=int(input("Enter number:"))
    square=num**2
    print("The square of the", num, "is",square)

print("Negative number entered!")

# Ask user to enter a long sentence , compute how many vowels are present I this sentence.
# Ensure that you consider both lower case and upper case are considered.

sentence=input("Enter a sentence: ").lower()
length=len(sentence)
index=0
vowels_count=0

vowels_dataset = "aeiou"

while(index<length):
    if(sentence[index] in vowels_dataset):
        vowels_count=vowels_count+1

    index=index+1


print("The number of vowels are: ",vowels_count)

# Write a program that takes a single long sentence from the user and computes the frequency of each vowel character (a, e, i, o, u).
# The program should store these frequencies in a dictionary where the keys are the vowels and the values are their respective counts.
# After computing the frequency, the program should display the dictionary.

vowels_dict={"a":0,"e":0,"i":0,"o":0, "u":0}
vowels_dataset="aeiou"
sentence=input("Enter a sentence: ").lower()
length=len(sentence)
index=0

while(index<length):
    if(sentence[index] in vowels_dataset):
        vowels_dict[sentence[index]]+=1

    index=index+1

print(vowels_dict)

sentence = input("Please enter a long sentence: ").lower()
Vowels = ["a", "e", "i", "o", "u"]

analysis = {}

index = 0
final_index = len(sentence)

while index < final_index :
    current_alphabet = sentence[index]
    if current_alphabet in Vowels :
        if current_alphabet not in analysis.keys()   :
            analysis[current_alphabet] = sentence.count(current_alphabet)
    index = index +1


print(analysis)

# Create a program that first asks the user how many movies are their favorites.
# Based on the number entered, the program should then prompt the user to input the names of that many movies.
# The movie names should be stored in a list.
# After collecting all the movie names, the program should walk through the list
# and print the length (number of characters) of each movie name.

fav_movies_count=999
movies=[]
count=0
fav_movies_count = int(input("How many movies are your favourite?: "))

while(count<fav_movies_count):
    movie_name=input("Enter the name of movie: ")
    movies.append(movie_name)
    count=count+1

final_pos=len(movies)
index=0

while(index<final_pos):
    print("The movie",movies[index],"has", len(movies[index]),"characters")
    index=index+

"""
#Article on Medium to traverse dictionary using while loop
# Dictionary representing monthly revenue for 2022
revenue_2022 = {
    "January": 15000,
    "February": 17000,
    "March": 16000,
    "April": 17500,
    "May": 18000,
    "June": 200000,
    "July": 19000,
    "August": 20000,
    "September": 18500,
    "October": 19500,
    "November": 21000,
    "December": 22000
}

# Dictionary representing monthly revenue for 2023
revenue_2023 = {
    "January": 21000,
    "February": 22000,
    "March": 23000,
    "April": 24000,
    "May": 25000,
    "June": 26000,
    "July": 27000,
    "August": 28000,
    "September": 29000,
    "October": 30000,
    "November": 31000,
    "December": 32000
}

# Question: You have the monthly revenue data for the years 2022 and 2023.
# Calculate the average revenue for the year 2022.
keys_2022=list(revenue_2022.keys())
final_pos_2022=len(keys_2022)
index_2022=0
sum_2022=0

while (index_2022<final_pos_2022):
    sum_2022=sum_2022+revenue_2022[keys_2022[index_2022]]
    index_2022=index_2022+1

avg_2022=sum_2022/len(keys_2022)
print("The average revenue for the year 2022 is: ",avg_2022)


# Calculate the average revenue for the year 2023.
keys_2023=list(revenue_2023.keys())
final_pos_2023=len(keys_2023)
index_2023=0
sum_2023=0
while (index_2023 < final_pos_2023):
    sum_2023 = sum_2023 + revenue_2023[keys_2023[index_2023]]
    index_2023=index_2023+1

avg_2023 = sum_2023 / len(keys_2023)
print("The average revenue for the year 2023 is: ", avg_2023)

# Based on the average revenue, determine which year had a better average revenue.
if(avg_2022>avg_2023):
    print(2022,"has better average revenue.")
else:
    print(2023, "has better average revenue.")