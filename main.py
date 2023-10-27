# Write your code below this line 👇

# import random

# random_int = random.randint(1, 10)
# print(random_int)

# random_float = random.random()
# print(random_float)

# states_of_america = ["Delaware", "Pennsylvania", "Ohio"]
# print(states_of_america[-1])

# names_str = input("write names: ")
# print(names_str)
# print(type(names_str))

# names = names_str.split(",")
# fruits = ["apple", "banana", "grape"]
# vegs = ["pototes", "spinach"]
# fruits_and_vegs = [fruits, vegs]
# print(fruits_and_vegs)
# print(fruits_and_vegs[1][1])

# print(names)
# print(type(names))

# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#   print(fruit)
# print(fruit)
# def greet(name):
#     print(f"Hi,{name} how are you?")

# greet("Sophie")


#Dictionaries
#Nesting
'''programming_dictionary = {
    "Bug": "An error in the program from runnng as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again,",}

print(programming_dictionary["Bug"])
# Adding new items to disctionary
programming_dictionary["Compile Error"] = "This is an error."
print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}
#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an itme in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting list and dictionaries
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany":["Berlin", "Hamburg", "Stuttgart"],
}

#travel_log = {
#    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12},
#    "Germany":{"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visited": 20},
#}

#print(travel_log["France"]["cities_visited"])

#Nesting Dictionary in al list

travel_log = [
    {"country": "France", 
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visited": 12
    },
    {"county": "Germany", 
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
     "total_visited": 20
    },
     ]
print(travel_log[0]["cities_visited"])


country = "Brazil" # Add country name
visits = 2 # Number of visits
list_of_cities = ["Sao Paulo", "Rio"] # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(visited_country, visited, list_of_cities):
    new_country = {}
    new_country["country"] = visited_country 
    new_country["visits"] = visited
    new_country["cities"] =list_of_cities
    
    travel_log.append(new_country)
        
    #print(travel_log)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
print(starting_dictionary)
starting_dictionary["c"] = 7
print(starting_dictionary)'''


    
        
       
