# Quiz Scoreboard

FILE_NAME = "quiz_scores.txt"

questions = [
    ("Which keyword defines a function in Python?", "def"),
    ("Which data type stores True or False?", "bool"),
    ("What is the output of 10 // 3?", "3"),
    ("Which method adds an item to a list?", "append"),
    ("Which loop repeats while a condition is true?", "while")
]


def play_quiz():
    name = input("Enter your name: ")
    score = 0

    print("\n===== PYTHON QUIZ =====")

    for question, answer in questions:
        print("\n" + question)
        user_answer = input("Your answer: ")

        if user_answer.lower().strip() == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! Answer:", answer)

    print("\nYour score:", score, "/", len(questions))

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{score}\n")

    print("Your score has been saved!")


def view_scores():
    try:
        with open(FILE_NAME, "r") as file:
            scores = file.readlines()

        if not scores:
            print("No scores available.")
            return

        print("\n===== SCOREBOARD =====")

        for record in scores:
            name, score = record.strip().split(",")
            print(name, "-", score, "points")

    except FileNotFoundError:
        print("No scoreboard found.")


def show_top_scorer():
    try:
        with open(FILE_NAME, "r") as file:
            scores = file.readlines()

        if not scores:
            print("No scores available.")
            return

        records = []

        for record in scores:
            name, score = record.strip().split(",")
            records.append((name, int(score)))

        top_scorer = max(records, key=lambda x: x[1])

        print("\n===== TOP SCORER =====")
        print("Name:", top_scorer[0])
        print("Score:", top_scorer[1])

    except FileNotFoundError:
        print("No scoreboard found.")


while True:
    print("\n===== QUIZ APPLICATION =====")
    print("1. Play Quiz")
    print("2. View Scores")
    print("3. Show Top Scorer")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        play_quiz()
    elif choice == "2":
        view_scores()
    elif choice == "3":
        show_top_scorer()
    elif choice == "4":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice!")
