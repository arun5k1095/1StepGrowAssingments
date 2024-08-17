movie_details = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Release_Year": 2010,
    "Genres": ["Action", "Sci-Fi", "Thriller"],
    "Cast": {
        "Leonardo DiCaprio": "Cobb",
        "Joseph Gordon-Levitt": "Arthur",
        "Elliot Page": "Ariadne",
        "Tom Hardy": "Eames"
    },
    "Duration_Minutes": 148,
    "Rating": 8.8,
    "Box_Office_Millions": 829.89
}

# 1 Update the rating to 9.0.
print(movie_details["Rating"])
movie_details["Rating"]=9.0
print(movie_details["Rating"])

# 2 Add a new key-value pair for "Budget" with a value of 3 160 million.
movie_details["Budget"]=3160000000
print(movie_details["Budget"])

# 4 Insert a new cast member into the nested dictionary.
# movie_details["Cast"]="Arun" -- the whole dictionary will be replaced/updated                                  by Arun i.e "Cast":"Arun"
#in dictionary, if i add Martha stewart, the key will be created.
movie_details["Cast"]["Martha Stewart"]="Lisa"
print(movie_details["Cast"])

# 5 Remove the "Box_Office_Millions" entry.
movie_details.pop("Box_Office_Millions")
print(list(movie_details.keys()))

# 6 Add "Mystery" to the genres list.
movie_details["Genres"].append("Mystery")
print(movie_details["Genres"])

# 7 Remove "Sci-Fi" from the genres list.
movie_details["Genres"].remove("Sci-Fi")
print(movie_details["Genres"])

print(list(movie_details.keys()))
print(movie_details)