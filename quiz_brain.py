# Create a class called QuizBrain
class QuizBrain:
    # Write an __init__() method
    def __init__(self, q_list):
        self.question_number = 0 # Initialize the question_number to 0
        self.score = 0
        self.question_list = q_list # Initialize the question_list to an input
    # Return a boolean depending on the value of question_number.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        ## vs. a long way of writing the code
        # if self.question_number >= len(self.question_list):
        #     return False
        # else:
        #     return True

    # Retrieve the item at the current question_number from the question_list
    def next_question(self):
        # Use the input() function to show the user the Question text and ask for the user's answer
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number} {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")


