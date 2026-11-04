

questions = {
    "1. Which language is used for AI?": "python",
    "2. What is the output of 5 + 5?": "10",
    "3. Which keyword is used to define a function?": "def",
    "4. Which data type stores True or False?": "bool",
    "5. Which loop runs while a condition is true?": "while"
}

score = 0

print("Welcome to the Python Quiz!")
print("----------------------------")

for question, answer in questions.items():
    print("\n" + question)

    user_answer = input("Your answer: ")

    if user_answer.lower() == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! Correct answer:", answer)

print("\n----- Quiz Results -----")
print("Your Score:", score, "/", len(questions))

if score == 5:
    print("Excellent performance!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("Keep learning and try again!")
