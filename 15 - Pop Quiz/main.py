"""Pop Quiz Game Simulator"""

from random import randint

from data import question_data
from question_model import Question


def get_quiz_length():
    """Asks user to establish number of questions to answer."""
    print("How many questions would you like in the quiz?")
    while True:
        length = input("Enter a number between 1 - 50: ")
        if not length.isdigit():
            print("You did not enter a numerical value: ")
        else:
            return int(length)


def pick_question():
    """Picks a question at random for the user."""
    while True:
        random_index = randint(0, len(question_data) - 1)
        question_to_ask = Question(
            question_data[random_index]["question"], question_data[random_index]["correct" "_answer"]
        )
        if random_index in indexes_used:
            continue
        else:
            indexes_used.append(random_index)
            return question_to_ask


def get_answer():
    """Asks the user to enter an answer to the question."""
    while True:
        answer = input("Type 'True' or 'False': ").lower()
        if answer == "true" or answer == "false":
            return answer
        else:
            print("You did not type 'True' or 'False'.")


QUESTIONS_ASKED = 0
indexes_used = []
CORRECT_ANSWERS = 0
quiz_length = get_quiz_length()
while QUESTIONS_ASKED < quiz_length:
    QUESTIONS_ASKED += 1
    question = pick_question()
    print(f"Q{QUESTIONS_ASKED}: {question.question}")
    user_answer = get_answer()
    if question.answer.lower() == user_answer:
        CORRECT_ANSWERS += 1
        print("You are correct!\n")
    else:
        print(f"You are wrong. The answer was: {question.answer}.\n")
print(f"Quiz finished. You got {CORRECT_ANSWERS} out of {quiz_length}.")
