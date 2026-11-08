# Text Analyzer

def analyze_text(text):

    words = text.split()

    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0

    for char in text:

        if char.lower() in "aeiou":
            vowels += 1

        elif char.isalpha():
            consonants += 1

        elif char.isdigit():
            digits += 1

        elif char == " ":
            spaces += 1

    print("\n----- Text Analysis -----")
    print("Total Words:", len(words))
    print("Total Characters:", len(text))
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Spaces:", spaces)


sentence = input("Enter a sentence: ")

analyze_text(sentence)
