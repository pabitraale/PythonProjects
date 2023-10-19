alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input("What is your message: \n").lower()
shift_number = int(input("What number you want to shift:\n "))
#encrypt function
def encrypt(text, number):
    encrypted_word=""
    for letter in text:
        letter_index = alphabet.index(letter)
        shift_num = letter_index + number
        encrypted_word += alphabet[shift_num]
    print("The encoded text is: ",encrypted_word)

#decrypt function
def decrypt(encrypted_text, number):
    decrypted_text =""
    for letter in encrypted_text:
        letter_index = alphabet.index(letter)
        shift_num = letter_index - number
        decrypted_text += alphabet[shift_num]
            
    print("The decoded text is: ", decrypted_text)


if direction == "encode":
    encrypt(message, shift_number)
elif direction == "decode":
    decrypt(message, shift_number)
    
