sentence = input("Enter a sentence: ")
vowels = 0
for char in sentence:
    if char in "aeiouAEIOU":
        vowels += 1
print("Number of vowels in the sentence: ", vowels)