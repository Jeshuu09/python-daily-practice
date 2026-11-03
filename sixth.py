# Simple Contact Book

contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone

        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        search_name = input("Enter name to search: ")

        if search_name in contacts:
            print("Phone number:", contacts[search_name])
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Try again.")
