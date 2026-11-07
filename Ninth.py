# Student Management System

students = []

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Class Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))

        student = {
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n----- Student Records -----")

            for student in students:
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                print("--------------------")

    elif choice == "3":
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("Student Found!")
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        if not students:
            print("No records available.")
        else:
            total = 0

            for student in students:
                total += student["marks"]

            average = total / len(students)

            print("Class Average:", round(average, 2))

    elif choice == "5":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice. Try again.")
