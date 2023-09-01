programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
    }

# retrieving item from dictionary
print(programming_dictionary["Bug"])

# Adding new item in dictionary
programming_dictionary["Loop"] = "There is an action doing something again and again"
print(programming_dictionary)

# create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
programming_dictionary = {}

# edit an item in a dictionary
programming_dictionary["Bug"] = "a moth in your computer "

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


"""
Nesting dictionary
"""

capitals = {
    "France": "paris",
    "Gremany": "berlin"
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["paris", "Lille", "Dijon"]
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["paris", "Lille", "Dijon"], "total_visits": 12},
}

# Nesting a dictionary in a list
travel_log = [
    {"country": "France",
     "cities_visited": ["paris", "Lille", "Dijon"],
     "total_visits": 12
     },
    {"country": "Germany",
     "cities_visited": ["paris", "Lille", "Dijon"],
     "total_visits": 6
     },

]



