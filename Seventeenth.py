# Employee Management System Using Inheritance

class Employee:

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary: Rs.", self.salary)


class Developer(Employee):

    def __init__(self, name, employee_id, salary, language):
        super().__init__(name, employee_id, salary)
        self.language = language

    def display_details(self):
        super().display_details()
        print("Programming Language:", self.language)


class Manager(Employee):

    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print("Department:", self.department)


employees = []

while True:

    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Developer")
    print("2. Add Manager")
    print("3. View Employees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        language = input("Enter programming language: ")

        employee = Developer(name, emp_id, salary, language)
        employees.append(employee)

        print("Developer added successfully!")

    elif choice == "2":
        name = input("Enter name: ")
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")

        employee = Manager(name, emp_id, salary, department)
        employees.append(employee)

        print("Manager added successfully!")

    elif choice == "3":
        if not employees:
            print("No employee records found.")
        else:
            for employee in employees:
                print("\n--------------------")
                employee.display_details()

    elif choice == "4":
        print("Exiting Employee Management System.")
        break

    else:
        print("Invalid choice!")
