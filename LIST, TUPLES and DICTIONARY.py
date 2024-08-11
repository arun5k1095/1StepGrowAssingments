
#Lists in Python
#Lists are mutable, meaning you can change their contents after creation. They are defined using square brackets [].
# Creating a list of fruits
fruits = ['Apple', 'Banana', 'Cherry']

# Accessing elements
first_fruit = fruits[0]  # Accessing the first element
second_fruit = fruits[1]  # Accessing the second element

print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
# Modifying an element in the list
fruits[1] = 'Blueberry'  # Changing 'Banana' to 'Blueberry'

print("Modified list:", fruits)
# Adding an element to the end of the list
fruits.append('Durian')

# Removing an element from the list
fruits.remove('Apple')

print("List after adding and removing elements:", fruits)

#Tuples in Python
#Tuples are immutable, meaning once they are created, their contents cannot be changed. They are defined using parentheses ().
# Creating a tuple of vegetables
vegetables = ['Carrot', 'Potato', 'Cucumber']

# Accessing elements
first_vegetable = vegetables[0]  # Accessing the first element
second_vegetable = vegetables[1]  # Accessing the second element

print("First vegetable:", first_vegetable)
print("Second vegetable:", second_vegetable)
# Trying to change an element in the tuple (this will raise an error)
try:
    vegetables[1] = 'Tomato'  # This will cause a TypeError
except TypeError as e:
    print("Error:", e)
# You can combine tuples using the + operator
fruits_tuple = ('Apple', 'Banana', 'Cherry')
# combined_tuple = fruits_tuple + vegetables
#
# print("Combined tuple:", combined_tuple)

#Dictionary in depth
#A dictionary in Python is an unordered collection of items where each item consists of a key-value pair.
# Dictionaries are defined using curly braces {}.
# Each key in a dictionary must be unique and is used to access the corresponding value.
#Dictionaries are collections of key-value pairs, and each key must be unique.
#You can access, add, modify, and remove items in a dictionary using keys.
#Dictionaries are useful when you need to associate specific values with specific keys, making data retrieval fast and easy.

# Creating a dictionary of student details
student = {
    'name': 'John Doe',
    'age': 20,
    'major': 'Computer Science'
}

# Accessing values using keys
name = student['name']  # Accessing the value associated with the key 'name'
age = student['age']  # Accessing the value associated with the key 'age'

print("Name:", name)
print("Age:", age)

# Adding a new key-value pair to the dictionary
student['grade'] = 'A'

# Modifying an existing key-value pair
student['age'] = 21

print("Updated student dictionary:", student)
# Removing a key-value pair using pop()
major = student.pop('major')

print("Removed major:", major)
print("Student dictionary after removal:", student)
# Iterating over keys and values in the dictionary
for key, value in student.items():
    print(f"{key}: {value}")
# Checking if a key exists in the dictionary
if 'name' in student:
    print("The key 'name' exists in the dictionary.")
else:
    print("The key 'name' does not exist in the dictionary.")


#Nested Dictionaries
# A dictionary containing another dictionary

university = {
    'name': 'XYZ University',
    'location': 'City ABC',
    'students': {
        'student1': {'name': 'John Doe', 'age': 20, 'major': 'Computer Science'},
        'student2': {'name': 'Jane Doe', 'age': 22, 'major': 'Mathematics'}
    }
}

# Accessing nested dictionary values
student1_name = university['students']['student1']['name']
student2_major = university['students']['student2']['major']

print("Student 1 Name:", student1_name)
print("Student 2 Major:", student2_major)
