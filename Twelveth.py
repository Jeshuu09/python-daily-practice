# Personal Notes Manager

FILE_NAME = "my_notes.txt"


def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

            if not notes:
                print("No notes available.")
            else:
                print("\n----- Your Notes -----")

                for i, note in enumerate(notes, start=1):
                    print(i, ".", note.strip())

    except FileNotFoundError:
        print("No notes file found.")


def search_note():
    keyword = input("Enter keyword to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for note in file:
                if keyword.lower() in note.lower():
                    print("Found:", note.strip())
                    found = True

            if not found:
                print("No matching note found.")

    except FileNotFoundError:
        print("No notes file found.")


while True:
    print("\n===== NOTES MANAGER =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        search_note()

    elif choice == "4":
        print("Thank you for using Notes Manager!")
        break

    else:
        print("Invalid choice!")
