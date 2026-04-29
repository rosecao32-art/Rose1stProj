import random
import string

def generate_password(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the Password Generator!")
length = int(input("Enter password length: "))
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

print("Your new password:", generate_password(length, use_digits, use_symbols))

def generate_random_string(length, characters=None):
    """
    Generate a random string of given length from the provided characters. 
    If characters is None, use letters (uppercase + lowercase) and digits.
    """
    # Validate length
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    # Default character set: letters + digits
    if characters is None:
        characters = string.ascii_letters + string.digits

    # Validate characters
    if not characters:
        raise ValueError("Characters set cannot be empty.")
    
    # Generate random string
    # return ''.join(random.choice(characters) for _ in range(length))
    return''.join(random.choices(characters, k=length))

# Example usage:
if __name__ == "__main__":
    try:
        length = 12
        random_str = generate_random_string(length)
        print(f"Random string ({length} chars): {random_str}")
    except ValueError as e:
        print(f"Error: {e}")

characters = string.ascii_letters + string.digits   # A-Z, a-z, 0-9
length = 10 # Desired string length

# Generate random string
random_string = ''.join(random.choices(characters, k=length))

print(f"Random 10 chars string: {random_string}")