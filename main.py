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
print(starting_dictionary)

#Functions with outputs
def format_name(f_name, l_name):
    
    first_name = f_name[0].upper()
    for i in range(1, len(f_name)):
        first_name += f_name[i].lower()
    
    last_name = l_name[0].upper()
    for i in range(1, len(l_name)):
        last_name += l_name[i].lower()
    print(f"{first_name} {last_name}")
        
format_name("pABITRA", "aLE")       
#title case
def format_name_usingTitle(f_name, l_name):

    print(f"{f_name.title()} {l_name.title()}")

format_name_usingTitle("pABITRA", "aLE") 

def format_name_titleCase(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

name = format_name_titleCase("pABITRA", "aLE") 
print(name)

#function with more than one return
def format_name_titleCase(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

name = format_name_titleCase(input("What is your first name?"), input("What is your last name?")) 
print(name)

#Docstrings
def format_name_titleCase(f_name, l_name):
    """Take a first and last name  and format it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

name = format_name_titleCase(input("What is your first name?"), input("What is your last name?")) 
print(name)'''

