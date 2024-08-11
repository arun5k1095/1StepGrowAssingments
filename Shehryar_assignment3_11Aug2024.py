sports=["Cricket", "Football", "Basketball", "Tennis", "Hockey"]

#Task 1
new_list=sports[:3]
print(new_list)

#Task 2
sports.append("Badminton")
print(sports)
#Task 3
sports.insert(3,"Swimming")
print(sports)

#Task 4
sports.remove("Tennis")
print(sports)


#Task 5
reverse_list=sports[::-1]
print(reverse_list)

#Task 6
pos=sports.index("Basketball")
print("Position of basketball: ",pos)

#Task 7
occurences_fb=sports.count("Football")
print("No. of occurences of football", occurences_fb)

#Task 8
outdoor_games = ['Golf', 'Rugby']
all_sports=sports+outdoor_games
print(all_sports)


