# Student Grade Calculator

name = input("Enter student name: ")

marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
