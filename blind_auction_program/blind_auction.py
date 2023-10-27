from replit import clear
import art

logo = art.logo
print(logo)

print("Welcome to the secret auction program.")
bidder = {}
#find highest bidder
def find_highest_bidder(bidder_dict):
    maxVal = 0
    bidder_name = ""
    for key in bidder_dict:
        if maxVal < bidder_dict[key]:
            maxVal = bidder_dict[key]
            bidder_name = key
    return bidder_name, maxVal


boolean_flag = True

while boolean_flag:
    name = input("What is your name?:")
    bid_amt = int(input("What's your bid?: $"))
    bidder[name] = bid_amt
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")

    if other_bidder == "yes":
        clear()   
    elif other_bidder == "no":
        winner_name = find_highest_bidder(bidder)[0]
        price = find_highest_bidder(bidder)[1]
        print(f"The winner is {winner_name} with a bid of ${price}")
        boolean_flag = False
    else:
        print("Invalid input. ")
        other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
        clear()
        

        
        


