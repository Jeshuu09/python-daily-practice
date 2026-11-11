# Password Generator

import random
import string

def generate_password(length):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length < 8:
    print("Password length must be at least 8 characters.")
else:
    password = generate_password(length)

    print("\nYour Generated Password:")
    print(password)
