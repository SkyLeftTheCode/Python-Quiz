# Python Quiz Game 📝

**Short Description:**  
A simple console-based multiple-choice quiz built with Python. Players answer a set of questions and get a score at the end.  

## Features
- Presents multiple-choice questions with 4 options each.  
- Player inputs their choice (A, B, C, or D).  
- Immediate feedback for correct or incorrect answers.  
- Displays the correct answers and final score at the end.  
- Calculates percentage score.  

## How to Use
1. Run the program using Python.
2. Read each question and the corresponding options.
3. Input your answer (A, B, C, or D) for each question.
4. View the results, including correct answers, your guesses, and your score.

## Built With
- Python 3  

## Code Example

```python
# Multiple Choice Quiz Game

questions = (
    "What is the data type of 'Hello'?",
    "Which operator is used for multiplication?",
    "Which keyword is used to define a function?",
    "Which function converts a string to an integer?",
    "Which method is used to add an item to a list?"
)

options = (
    ("A. int", "B. str", "C. float", "D. bool"),
    ("A. +", "B. -", "C. *", "D. /"),
    ("A. func", "B. define", "C. def", "D. function"),
    ("A. str()", "B. int()", "C. float()", "D. char()"),
    ("A. add()", "B. append()", "C. insert()", "D. extend()")
)

answers = ("B", "C", "C", "B", "B")
guesses = []
score = 0
numberOfQuestion = 0

for question in questions:
    print("-"*50)
    print(question)
    print("-"*50)
    for option in options[numberOfQuestion]:
        print(option)
    choice = input("Please enter your choice: ").upper()
    guesses.append(choice)
    if choice == answers[numberOfQuestion]:
        print("CORRECT!")
        score += 1
    else:
        print(f"Wrong answer, the correct answer is {answers[numberOfQuestion]}")
    numberOfQuestion += 1

def resultdisplay():
    print("-"*50)
    print(" "*20 + "RESULT")
    print("-"*50)
    print("Answers : ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()
    print("Guesses : ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()
    print(f"Your score is: {score}/{len(questions)} ({score/len(questions)*100}%)")

resultdisplay()
