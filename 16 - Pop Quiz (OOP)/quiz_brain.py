"""Quiz Brain Class Module"""


class QuizBrain:
    """Quiz Brain Class"""
    def __init__(self, q_list, q_number=0, score=0):
        self.q_list = q_list
        self.q_number = q_number
        self.score = score

    def still_has_questions(self):
        """Checks if the game still has questions"""
        return self.q_number < len(self.q_list)

    def next_q(self):
        """Provides Next Question"""
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_q.q_text} (True or False): ")
        self.check_answer(user_answer, current_q.q_answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks given answer"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct.")
        else:
            print("Incorrect.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score} out of {self.q_number}\n")
