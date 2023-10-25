import art
logo = art.logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input("What is your message: \n").lower()
shift_number = int(input("What number you want to shift:\n "))
shift_number = shift_number % 26

def caesar(text, shift_num, cipher_direction):
   
    final_word=""
    if cipher_direction == "decode":
        shift_num *= -1
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter_index = letter_index + shift_num
            final_word += alphabet[new_letter_index]
        else:
            final_word += letter
        
    print(f"The {cipher_direction}d text is: {final_word}") 
    
caesar(message, shift_number, direction)  
#if user want to play again or not

boolean_flag = True
while boolean_flag:
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if play_again == 'no'.lower():
        boolean_flag = False
        print("Goodbye")
        break
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("What is your message: \n").lower()
    shift_number = int(input("What number you want to shift:\n "))
    shift_number = shift_number % 26
    
    caesar(message, shift_number, direction)
    
        
        

    