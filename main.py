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
import random
from replit import clear

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif player_score == 0:
        return "You win. You have a Blackjack"
    elif computer_score > 21:
        return "You Win."
    elif player_score > computer_score:
        return "Computer win"
    else:
        return "You lose"

def play_blackjack():
    
    #computer and user gets 2 cards each
    player_cards = []
    computer_cards = []
    
    for num in range(0, 2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    print("player cards: ", player_cards)
    print("computer cards: ", computer_cards)
    
    def calculate_score(cards):
        """Take a list of cards and return calculate card"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0    
        elif sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            
        return sum(cards)
        
    game_over = False
    
    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score is: {player_score} ")
        print(f"computer's first card: {computer_cards[0]} ")
    
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else: 
            add_card = input("Do you want to get another card? Type 'yes' or 'no': ")
            if add_card == "yes".lower():
                player_cards.append(deal_card())
                print("player cards: ", player_cards)
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final cards: {player_cards}, and final socre is: {player_score}")
    print(f"Computer final cards: {computer_cards}, and final socre is: {computer_score}")
    print(compare(player_score, computer_score) )  
    
play_blackjack() 

play_again = input("Do you want to play again? Type 'yes' or 'no': ")
if play_again == 'yes'.lower():
    clear()
    play_blackjack()


    