alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#user input
encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
message = input("What is your message: \n").lower()
shift_number = int(input("What number you want to shift:\n "))
#encrypt 
def encrypt(text, number):
    encrypted_word=""
    for letter in text:
        letter_index = alphabet.index(letter)
        shift_num = letter_index + number
        if shift_num > 25:
            extra_num = shift_num - 26
            encrypted_word += alphabet[extra_num]
        else:
            encrypted_word += alphabet[shift_num]
    print("The encoded text is: ",encrypted_word)

encrypt(message, shift_number)



