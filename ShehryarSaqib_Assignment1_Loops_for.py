scoresCard=[5,10,15,20]
total=0

for score in scoresCard:
    # print(score)
    total=total+score
    # print("Sherry")
print(total)

statement="washington dc is in united states of america"
vowels="aeiou"

for character in statement:
    if character in vowels:
        print(character)

#for loop for dictionary
# total_2022=0
# for month in revenue_2022.keys():
#     total_2022=total_2022+revenue_2022[month]

for i in range(5):
    num1 = input("Enter your score 1:")
    num2 = input("Enter your score 2:")
    result = num1 + num2
    print("The total sum is :", result)


# Ask user for a number. Print all the numbers until that number using while loop.
number=int(input("Please enter a number: "))

for i in range(number+1):
    print(i)

# Ask user for a number  , starting this numbers , all the way upto 0 , print all the numbers in reverse order.
number=int(input("Please enter a number: "))

for i in range(number+1,-1,-1):
    print(i)

# Ask user for  number , and starting from 0 all way to this number , you must add up all the numbers
# and print the result

result=0
input_number=int(input("Please enter a number: "))
current_num=0


for i in range(input_number+1):
    result=result+i

print(result)

# Create a program that continuously asks the user to input a number and then prints the square of that number.
# The program should keep running until the user inputs a negative number.
# Once a negative number is entered, the program should stop.

for _ in range(1,999):
    num=int(input("Enter number:"))

    if num<0:
        print("Negative number entered!")
        break

    square = num ** 2
    print("The square of the", num, "is", square)

# Ask user to enter a long sentence , compute how many vowels are present I this sentence.
# Ensure that you consider both lower case and upper case are considered.

sentence=input("Enter a sentence: ").lower()
length=len(sentence)
index=0
vowels_count=0

vowels_dataset = "aeiou"

for index in range(length):
    if sentence[index] in vowels_dataset:
        vowels_count=vowels_count+1

print("The number of vowels are: ",vowels_count)

# Write a program that takes a single long sentence from the user and computes the frequency of each vowel character (a, e, i, o, u).
# The program should store these frequencies in a dictionary where the keys are the vowels and the values are their respective counts.
# After computing the frequency, the program should display the dictionary.

vowels_dict={"a":0,"e":0,"i":0,"o":0, "u":0}
vowels_dataset="aeiou"
sentence=input("Enter a sentence: ").lower()
length=len(sentence)

for index in range(length):
    if sentence[index] in vowels_dataset :
        vowels_dict[sentence[index]]+=1

print(vowels_dict)

sentence = input("Please enter a long sentence: ").lower()
Vowels = ["a", "e", "i", "o", "u"]

analysis = {}

final_index = len(sentence)

for index in range(final_index):
    current_alphabet = sentence[index]
    if current_alphabet in Vowels :
        if current_alphabet not in analysis.keys()   :
            analysis[current_alphabet] = sentence.count(current_alphabet)


print(analysis)

# Create a program that first asks the user how many movies are their favorites.
# Based on the number entered, the program should then prompt the user to input the names of that many movies.
# The movie names should be stored in a list.
# After collecting all the movie names, the program should walk through the list
# and print the length (number of characters) of each movie name.

movies=[]
fav_movies_count = int(input("How many movies are your favourite?: "))

for _ in range(fav_movies_count):
    movie_name=input("Enter the name of movie: ")
    movies.append(movie_name)

final_pos=len(movies)
index=0

for index in range(final_pos):
    print("The movie",movies[index],"has", len(movies[index]),"characters")

