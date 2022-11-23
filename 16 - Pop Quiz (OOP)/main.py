"""Pop Quiz Game Simulator"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    QUESTION = item["text"]
    ANSWER = item["answer"]
    new_q = Question(QUESTION, ANSWER)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_q()
print("Quiz finished.")
print(f"Your final score was {quiz.score} / {quiz.q_number}")
