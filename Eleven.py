# Library Management System

books = []

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")

        book = {
            "name": name,
            "issued": False
        }

        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if not books:
            print("No books available.")
        else:
            print("\n----- Book List -----")

            for i, book in enumerate(books, start=1):
                status = "Issued" if book["issued"] else "Available"
                print(i, book["name"], "-", status)

    elif choice == "3":
        name = input("Enter book name to issue: ")

        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True

                if not book["issued"]:
                    book["issued"] = True
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")

                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        name = input("Enter book name to return: ")

        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True

                if book["issued"]:
                    book["issued"] = False
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")

                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        print("Thank you for using the Library System!")
        break

    else:
        print("Invalid choice. Try again.")
