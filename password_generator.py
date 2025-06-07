import random
import string

def generate_password(length=12, use_digits=True, use_special=True, use_upper=True, use_lower=True):
    characters = ""
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase

    if not characters:
        return "No character types selected!"

    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    print("🔐 Password Generator")
    length = int(input("Enter password length: "))
    
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_special, use_upper, use_lower)
    print(f"\nGenerated Password: {password}")
