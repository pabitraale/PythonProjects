#This will calculate bills with tip
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
total_people = input("How many people to split the bill? ")
#convert all string input to int
bill_float = float(total_bill)
people_int = int(total_people)
tip_int = int(tip_percent)
#calculate tip
total_tip = bill_float * tip_int/100
#calculate per person bill
per_person_bill = (bill_float + total_tip)/people_int 

print(f"Each person should pay: {round(per_person_bill, 2)}")
