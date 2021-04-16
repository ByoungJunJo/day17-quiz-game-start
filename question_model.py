# TODO 1. Create a 'Question' class with an __init()__method with two attributes: 'text' and 'answer' attribute
class Question:
    # Create a constructor
    def __init__(self, q_text, q_answer):
        # Create the two attributes 'answer' and 'text'. In order to do that, I need to declare self
        self.text = q_text
        self.answer = q_answer

# # Test class by creating an object
# new_q = Question("hello world", "true")
# print(new_q.text)