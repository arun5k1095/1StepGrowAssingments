sentence=input("Enter a sentence: ")
uppercase=sentence.upper()
print("Name in uppercase: ", uppercase)

length=len(sentence)
first_half=sentence[:length//2]
print("First half os sentence is: ", first_half)

full_name=input("Enter your full name: ")
reverse=full_name[::-1]
print("Full name in reverse is: ", reverse)

vowels="aeiouAEIOU"
for vowel in vowels:
    sentence=sentence.replace(vowel,'#')

print("Replaced with vowels sentence: ",sentence)

emailid=input("Enter emailid: ")
index=emailid.index("@")
user_name=emailid[:index]
print(user_name)

sentence2=input("Enter a sentence: ")
count_vowels=0
for vowel in vowels:
    ind_count=sentence2.count(vowel)
    count_vowels+=ind_count

print(count_vowels)


