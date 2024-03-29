import random
import string

def generate_password(length=12):
    
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = letters + digits + special_characters

    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
