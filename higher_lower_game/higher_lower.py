from art import logo, vs
import data
import random
from replit import clear

print(logo)

get_data = data.data
#Generate one random data to start a game
def get_random_data(data):
    random_data = random.choice(get_data)
    return random_data

#compare the follower
def compare_follower(data1_follower, data2_follower):
    if data1_follower > data2_follower:
        return "A".lower()
    else:
        return "B".lower()
        
right_score = 0
wrong_score = 0
data1 = get_random_data(get_data)  #get first data
while wrong_score  < 1: 
    print(f"Compare A: {data1['name']}, {data1['description']}, from {data1['country']}.")
    print(vs)
    data2 = get_random_data(get_data) 
    if data1 == data2:
        data2 = get_random_data(get_data) 
       
    print(f"Against B: {data2['name']}, {data2['description']}, from {data2['country']}.")
    
    has_more_follower = compare_follower(data1['follower_count'], data2['follower_count'])
    #print("more follower: ", has_more_follower)
    #Ask the user who has more follower
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    #Compare whether user got score or not
    if has_more_follower == "a" and user_choice == "a":
        right_score += 1
    elif has_more_follower == "a" and user_choice == "b":
        wrong_score += 1
    elif has_more_follower == "b" and user_choice == "a":
        wrong_score += 1
    else:
        right_score += 1
        
    #Replace first data to second data
    data1 = data2
    clear()
    print(logo)
    #print score if user gives right and wrong answer
    if wrong_score == 1:
        print(f"Sorry, that's wrong. Final score:{right_score}")
    else:
        print(f"You're right! Current score: {right_score}")



  