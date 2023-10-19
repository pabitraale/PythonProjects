alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input("What is your message: \n").lower()
shift_number = int(input("What number you want to shift:\n "))

def caesar(text, shift_num, cipher_direction):
   
    final_word=""
    for letter in text:
        letter_index = alphabet.index(letter)
        if cipher_direction == "decode":
            shift_num *= -1
        new_letter_index = letter_index + shift_num
        final_word += alphabet[new_letter_index]
    print(f"The {cipher_direction}d text is {final_word}") 
    
caesar(message, shift_number, direction)        
