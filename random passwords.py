'''
Creating a number of random passwords of a certain length
using 'Random' library
'''

import random

passwords_count = 100
length = 50

def generate():
	lowercase_letters = 'abcdefghijklmnopqrstuvwxyz' # lowercase_letters
	uppercase_letters = lowercase_letters.upper() # uppercase_letters
	digits = '1234567890' # digits
	signs = '`!@#$%^&*()-_=+\|[]{};:<>,.?/' # signs

	password = ''
	symbols_type = ['lowercase_letters', 'uppercase_letters', 'digits', 'signs']

	for i in range (length):
		if random.choice(symbols_type) == symbols_type[0]: # lowercase_letters
			password += random.choice(lowercase_letters)
		elif random.choice(symbols_type) == symbols_type[1]: # uppercase_letters
			password += random.choice(uppercase_letters)
		elif random.choice(symbols_type) == symbols_type[2]: # digits
			password += random.choice(digits)
		else: # signs
			password += random.choice(signs)
	return password		

def main():
	passwords = []
	while (len(passwords) < passwords_count):
		password = generate()
		if password not in passwords:
			passwords.append(password)
	for i in range(10):
		print(passwords[i])			

main()