#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Taking user input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Taking random choices from the lists letters, symbols, and numbers and storing them in variables
password_letters = random.choices(letters, k = nr_letters)
password_symbols = random.choices(symbols, k = nr_symbols)
password_numbers = random.choices(numbers, k = nr_numbers)
# Adding letters, symbols and numbers to one list
password_list = password_letters + password_symbols + password_numbers
#Randomizing the list
random.shuffle(password_list)
#Converting list output to string
separator = ''
password = separator.join(password_list)
print(f"Your generated password is: {password}")

