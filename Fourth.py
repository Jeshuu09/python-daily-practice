# Password Strength Checker

password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password! Must contain at least 8 characters.")
elif not any(char.isdigit() for char in password):
    print("Weak password! Add at least one number.")
elif not any(char.isupper() for char in password):
    print("Weak password! Add at least one uppercase letter.")
else:
    print("Your password is strong!")
