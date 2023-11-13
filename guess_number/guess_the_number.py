import random
import art
logo = art.logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_num = random.randint(1, 100)
print(f"The number is: {random_num}")
choosen_level = input("Choose a difficult. Type 'easy' or 'hard':")

#Based on difficulty level set the number of attempts
if choosen_level == "easy":
    number_of_attempt = 8
else:
    number_of_attempt = 5

#loop until guess number is right or number of attempts is not 0
while number_of_attempt >= 0:
    print(f"You have {number_of_attempt} attempts remaining to guess the number.")
    
    if number_of_attempt == 0:
        print("You've run out of guesses, you lose.")
        break
        
    guess_number = int(input("Make a guess: "))

    if random_num == guess_number:
        print(f"You got it! The answer was {guess_number}.")
        break
    elif guess_number > random_num:
        print("Too high.")
        number_of_attempt -= 1
        print("Guess again.")
    else:
        print("Too low.")
        number_of_attempt -= 1
        print("Guess again.")
    









