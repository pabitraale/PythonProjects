import random
import hangman_art
import hangman_words

stages = hangman_art.stages
word_list = hangman_words.word_list

#Get random number from the list
rand_num = random.randint(0,len(word_list)-1)
#Use that random numbert to pick the word from the list
chosen_word = word_list[rand_num]
life = 6
logo = hangman_art.logo
print(logo)
print("Welcome to the Hangman Game!")

display = []
# Create list having _ for each letter in the word
for _ in range(len(chosen_word)):
        display += "_"
# Loop until word is complete
end_game = False
while not end_game:
    #Ask user to enter the guess letter
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed the letter{guess}.")

    #check if guess letter in the chosen word or not
    #If guessed letter in the chosen word than 
    #replace the _ with the guess letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            #chosen_word_length -= 1
    #Check if the guess letter is in the chosen word or not
    #if not reduce the life by 1 
    #if life is 0 then end the game
    if guess not in chosen_word:
        print(f"Your letter is {guess}. That's not in the word. You lose a life.")
        life -= 1
        print(stages[life])
        if life == 0:
            end_game = True
            print("You lose.")
            print("The word is:", chosen_word)

    print(f"{' '.join(display)}")
    #check if display is complete or not
    if "_" not in display:
        end_game = True
        print("You win.")

    
    





