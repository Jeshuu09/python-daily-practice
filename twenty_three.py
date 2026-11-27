# Email and Phone Number Validator

import re


def validate_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True

    return False


def validate_phone(phone):

    pattern = r'^[6-9]\d{9}$'

    if re.match(pattern, phone):
        return True

    return False


while True:

    print("\n===== VALIDATION SYSTEM =====")
    print("1. Validate Email")
    print("2. Validate Phone Number")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        email = input("Enter email address: ")

        if validate_email(email):
            print("Valid email address!")
        else:
            print("Invalid email address!")

    elif choice == "2":

        phone = input("Enter phone number: ")

        if validate_phone(phone):
            print("Valid Indian mobile number!")
        else:
            print("Invalid mobile number!")

    elif choice == "3":
        print("Exiting Validation System!")
        break

    else:
        print("Invalid choice!")
