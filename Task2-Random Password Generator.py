import random
import string

def password_generator(length, letters=True, numbers=True, symbols=True):
    characters = ""

    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Error: You must include at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    try:
        length = int(input("Enter the password length: "))
        letters = input("Do you want to include letters? (y/n): ").lower() == 'y'
        numbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'
        symbols = input("Do you want to include symbols? (y/n): ").lower() == 'y'

        return length, letters, numbers, symbols

    except ValueError:
        print("Error: Password length must be in Positive Integers.")
        return None

def main():
    user_input = get_user_input()

    if user_input:
        length, letters, numbers, symbols = user_input
        password = password_generator(length, letters, numbers, symbols)

        if password:
            print("Your generated password is :", password)

if __name__ == "__main__":
    main()