# List of questions
questions = (
    "What is the data type of 'Hello'?",
    "Which operator is used for multiplication?",
    "Which keyword is used to define a function?",
    "Which function converts a string to an integer?",
    "Which method is used to add an item to a list?"
)

# List of options (list of lists)
options = (
    ("A. int", "B. str", "C. float", "D. bool"),
    ("A. +", "B. -", "C. *", "D. /"),
    ("A. func", "B. define", "C. def", "D. function"),
    ("A. str()", "B. int()", "C. float()", "D. char()"),
    ("A. add()", "B. append()", "C. insert()", "D. extend()")
)

# List of correct answers (A-D)
answers = ("B", "C", "C", "B", "B")
gueesses = []

score = 0
numberOfQuestion = 0

for question in questions:
    print("-"*50)
    print(question)
    print("-"*50)

    for option in options[numberOfQuestion]:
        print(option)

    choice = input("Please enter your choice : ").upper()
    gueesses.append(choice)

    if choice == answers[numberOfQuestion]:
        print("CORRECT!")
        score += 1
    else:
        print(
            f"Wrong answer, the correct answer is {answers[numberOfQuestion]}")

    numberOfQuestion += 1


def resultdisplay():
    print("-"*50)
    print(" "*20 + "RESULT")
    print("-"*50)

    print("Answer : ", end="")

    for answer in answers:
        print(answer, end="")
    print()

    print("Guesses : ", end="")

    for guess in gueesses:
        print(guess, end="")
    print()

    print(
        f"Your score is: {score}/{len(questions)} ({score/len(questions)*100}%)")


resultdisplay()
