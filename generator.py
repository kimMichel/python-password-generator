import string
import random

letters = list(string.ascii_lowercase + string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

print('Welcome to the PyPAssword Generator!')

letters_number = int(input('How many letters would you like in your password? '))
num_number = int(input('How many symbols would you like? '))
symbols_number = int(input('How many numbers would you like? '))

random_letters = [random.choice(letters) for _ in range(letters_number)]
random_numbers = [random.choice(numbers) for _ in range(num_number)]
random_symbols = [random.choice(symbols) for _ in range(symbols_number)]

combined_list = random_letters + random_numbers + random_symbols
random.shuffle(combined_list)

random_string = ''.join(combined_list)

print(random_string)