# Shape Area Calculator Using Polymorphism

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth


class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


shapes = []

while True:

    print("\n===== SHAPE AREA CALCULATOR =====")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Display All Areas")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        shapes.append(Circle(radius))
        print("Circle added!")

    elif choice == "2":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        shapes.append(Rectangle(length, breadth))
        print("Rectangle added!")

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        shapes.append(Triangle(base, height))
        print("Triangle added!")

    elif choice == "4":
        if not shapes:
            print("No shapes available.")
        else:
            for shape in shapes:
                print("Area:", round(shape.calculate_area(), 2))

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
