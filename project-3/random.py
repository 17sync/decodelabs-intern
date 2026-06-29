import random
import string


def generatePassword(): pass
def menu(): pass


def menu():
    while True:
        print("\n===== RANDOM PASSWORD GENERATOR =====")
        print("1. Generate Password")
        print("2. Exit")

        operation=input("Choose an Operation: ")

        if operation=="1":
            generatePassword()

        elif operation=="2":
            print("\nThank you for using my Password Generator!")
            break

        else:
            print("Invalid input, try again.\n")


def generatePassword():
    try:
        length=int(input("Enter password length: "))

        if length<4:
            print("Password length must be at least 4.\n")
            return

        useSpecial=input("Include special characters? (Y/N): ").strip().lower()
        characters=string.ascii_letters+string.digits

        if useSpecial=="y":
            characters+=string.punctuation

        password=[
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits)
        ]

        if useSpecial=="y" or useSpecial=="Y":
            password.append(random.choice(string.punctuation))

        while len(password)<length:
            password.append(random.choice(characters))
        random.shuffle(password)

        print("\nGenerated Password:")
        print("".join(password))
        print()

    except ValueError:
        print("Please enter a valid number.\n")


menu()