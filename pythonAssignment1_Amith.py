# Ask user to enter a long sentence. Convert the whole sentence into upper case and print the result.
sentence = input("Enter a long sentence: ")
upper_case_sentence = sentence.upper()
print("Upper case sentence:", upper_case_sentence)

# Ask user to enter his full name, reverse the full name and print it.
full_name = input("Enter your full name: ")
reversed_name = full_name[::-1]
print("Reversed full name:", reversed_name)

# Ask user to enter a long sentence, print only the first half of the sentence.
half_sentence = sentence[:len(sentence)//2]
print("First half of the sentence:", half_sentence)

# Ask user to enter a long sentence, Replace all the occurrences of vowels with #, and print the modified content.
vowels = "AEIOUaeiou"
modified_sentence = ''.join(['#' if char in vowels else char for char in sentence])
print("Modified sentence:", modified_sentence)

# Ask user to enter his email id, fetch the user name from the string and print it.
email_id = input("Enter your email ID: ")
username = email_id.split('@')[0]
print("Username from email ID:", username)

# Ask user to enter a long sentence, count the total number of vowels that are present in the sentence.
vowel_count = sum([1 for char in sentence if char in vowels])
print("Total number of vowels in the sentence:", vowel_count)
