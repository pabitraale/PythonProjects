import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
letter_num = int(input("How many letters would you like in your password? \n"))
symbols_num = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))
#generate random letters and append to randompassword list variable
randomPasswordList = []
for i in range(0, letter_num):
  l = random.randint(0, len(letters)-1)
  randomPasswordList.append(letters[l])

#generate random symbols and append to randompassword list variable
for i in range(0, symbols_num):
  s = random.randint(0, len(symbols)-1)
  randomPasswordList.append(symbols[s])

#generate random numbers and append to randompassword list variable
for i in range(0, num):
  n = random.randint(0, len(numbers)-1)
  randomPasswordList.append(numbers[n])

#connecting list into one string password
password =''.join(randomPasswordList)

#shuffling password
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)
print("Your password is:", final_password)