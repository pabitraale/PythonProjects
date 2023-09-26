print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
cross_road = input("""You're at a cross road. Where do you want to go? Type "left" or "right"\n""")

if(cross_road.lower() == "right"):
  print("Fall into the lake. Game Over.")
else:
  swim_or_wait = input("""You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n""")
  if swim_or_wait.lower() == "wait":
    choose_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
    if choose_color.lower() == "red":
      print("Burned by fire. Game Over")
    elif choose_color.lower() == "blue":
      print("Eaten by beasts. Game Over")
    elif choose_color.lower() == "yellow":
      print("You Win!")
    else:
      print("Game Over")
  else:
    print("Attacked by a corcodile. Game Over")
  


