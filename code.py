import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid integer for the length.")
        return

    # Check if the length is non-negative
    if length <= 0:
        print("Please enter a positive integer for the length.")
        return

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
