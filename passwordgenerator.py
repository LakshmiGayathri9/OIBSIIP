
import random
import string
length = int(input("Enter length of the password: "))
letters = input("Do you want to include letters? (y/n): ").lower() == 'y'
numbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'
symbols = input("Do you want to include symbols? (y/n): ").lower() == 'y'

characters = ""

if letters:
    characters += string.ascii_letters
if numbers:
    characters += string.digits
if symbols:
    characters += string.punctuation

if not characters:
    print("Please select at least one character set.")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)


