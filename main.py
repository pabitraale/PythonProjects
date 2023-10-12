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
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["ardvark", "baboon", "camel"]

#Get random number from the list
rand_num = random.randint(0,len(word_list)-1)
#Use that random numbert to pick the word from the list
chosen_word = word_list[rand_num]
print(chosen_word)
lives = 6

display = []
# Create list having _ for each letter in the word
for _ in range(len(chosen_word)):
        display += "_"
# Loop until word is complete
end_game = False
while not end_game:
    #Ask user to enter the guess letter
    guess = input("Guess a letter: ").lower()
    #check if guess letter in the chosen word or not
    #If guessed letter in the chosen word than 
    #replace the _ with the guess letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            #chosen_word_length -= 1

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    #check if display is complete or not
    if "_" not in display:
        end_game = True
        print("You win.")

    print(stages[lives])
        

  


