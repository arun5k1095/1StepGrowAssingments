#Given the list sports = ['Cricket', 'Football', 'Basketball', 'Tennis', 'Hockey'], how would you access the first two and last elements of the list?

sports = ['Cricket', 'Football', 'Basketball', 'Tennis', 'Hockey']

# Accessing the first two elements
first_two = sports[:2]
print("First two elements:", first_two)

# Accessing the last element
last_element = sports[-1]
print("Last element:", last_element)


#Using the sports list, how would you create a new list containing the first three sports?
# Creating a new list with the first three sports
first_three_sports = sports[:3]
print("First three sports:", first_three_sports)

#How would you add the sport 'Badminton' to the sports list?
# Adding 'Badminton' to the list
sports.append('Badminton')
print("Updated sports list:", sports)

#How would you insert the sport 'Swimming' at the third position in the sports list?
# Inserting 'Swimming' at the third position (index 2)
sports.insert(2, 'Swimming')
print("Sports list after insertion:", sports)

#If you want to remove 'Tennis' from the sports list, which method would you use, and how would you write it?
# Removing 'Tennis' from the list
sports.remove('Tennis')
print("Sports list after removing Tennis:", sports)

#How would you reverse the order of elements in the sports list?
# Reversing the list
sports.reverse()
print("Reversed sports list:", sports)

# Another way to do the above is  , although what you did is correct , just another aproach below :
sports_reversed = sports[::-1]
print("Reversed sports list:", sports_reversed)

#______________________________________

#How would you find the index of 'Basketball' in the sports list?
# Finding the index of 'Basketball'
basketball_index = sports.index('Basketball')
print("Index of Basketball:", basketball_index)

#If the sports list had multiple occurrences of 'Football', how would you count how many times 'Football' appears in the list?
# Counting the occurrences of 'Football'
football_count = sports.count('Football')
print("Number of times Football appears:", football_count)

#How would you combine the sports list with another list called outdoor_games = ['Golf', 'Rugby']?
outdoor_games = ['Golf', 'Rugby']

# Combining the two lists
combined_list = sports + outdoor_games
print("Combined list:", combined_list)
