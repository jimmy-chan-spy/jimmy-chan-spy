import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters  # Uppercase & lowercase letters
    
    if use_digits:
        characters += string.digits  # Add numbers 0-9
    
    if use_specials:
        characters += string.punctuation  # Add special characters
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter password length: "))
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_specials = input("Include special characters? (y/n): ").lower() == 'y'

# Generate password
generated_password = generate_password(length, use_digits, use_specials)
print("\nGenerated Password:", generated_password)