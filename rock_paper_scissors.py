import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
your_num = int(input("What do you choose? Type 0 for Rock, 1, for Paper or 2 for Scissors.\n"))
if your_num == 0:
  print(rock)
elif your_num == 1:
  print(paper)
else:
  print(scissors)

computer_num = random.randint(0,2)
print("Computer chose: ")

if computer_num == 0:
  print(rock)
elif computer_num == 1:
  print(paper)
else:
  print(scissors)

if your_num > 2 or your_num < 0:
    print("Invalid input.")
elif your_num == 0 and computer_num == 2:
    print("You win!")
elif your_num == 2 and computer_num == 0:
    print("You lose")
elif your_num < computer_num:
    print("You lose")
elif your_num > computer_num:
    print("You win!")
elif your_num == computer_num:
    print("It's a draw.")
