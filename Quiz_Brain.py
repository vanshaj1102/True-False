class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list  # Renamed variable
        self.score = 0  # Added score as an instance variable

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        self.question_no += 1  # Move increment before printing
        current_question = self.question_list[self.question_no - 1]
        user_answer = input(f"Q. {self.question_no}: {current_question.text} (True/False): ")
        self.check_answers(user_answer, current_question.answer)

    def check_answers(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Woohoo!! That is correct 🎉")
            self.score += 1  # Score persists across questions
        else:
            print("This is the wrong answer ❌")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your Score: {self.score}/{self.question_no}")
        print(" \n ")

