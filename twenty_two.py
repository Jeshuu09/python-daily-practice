# Student Records Management Using JSON

import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n----- STUDENT RECORDS -----")

    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])
        print("----------------------")


def search_student():
    students = load_students()

    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


while True:

    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            add_student()
        except ValueError:
            print("Please enter valid marks.")

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Exiting Student Management System!")
        break

    else:
        print("Invalid choice!")
