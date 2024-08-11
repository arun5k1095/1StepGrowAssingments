

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


#Assignment 3
# Ask user to enter a long sentence. Convert the whole sentence into upper case and print the result.
sentence = input("Please enter a long sentence : ")
print("Your sentence in upper case is shown as: ", sentence.upper())


# Ask user to enter his full name , reverse the full name and print it.
full_name = input("Please enter your full name : ")
print("Your name in reverse order is: ", full_name[: :-1])


#Ask user to enter a long sentence , print only the first half of the sentence.
sentence = input("Please enter a long sentence : ")
end = int(len(sentence)/2)
print("Half of the sentence entered is shown as: ", sentence[:end:])


# Ask user to enter a long sentence , Replace all the occurences of vowels with # , and print the modified content.
sentence = input("Please enter a long sentence: ")
print("Your sentence replacing all vowels with # is shown as: ", sentence.lower().replace("a","#").replace("e","#").replace("i","#").replace("o","#").replace("o","#").replace("u","#"))


# Ask user to enter his email id , fetch the user name from the string and print it.
email = input("Please enter your email address: ")
end = email.index("@")
print("Your name extracted from email address is: ", email[:end:])

# Ask user to enter a long sentence , count the total number of Vowels that are present in the sentence.
sentence = input("Please enter a long sentence: ").lower()
vowels = sentence.count("a")
vowels = vowels + sentence.count("e")
vowels = vowels + sentence.count("i")
vowels = vowels + sentence.count("o")
vowels = vowels + sentence.count("u")
print("Count of vowels in your sentence is: ", vowels)


# Ask user to provide email id and fetch domain from it
email = input("Please enter your email address: ")
print(email.split("@")[-1].split(".")[0])


