

class Conditional_Node:
    def __init__(self, condition, child_question = None):
        self.condition = condition
        self.child_question = child_question

    def set_child_question(self, question):
        self.child_question = question

class Question_Node:
    def __init__(self, question, left_child = None, right_child = None):
        self.question = question
        self.left_child = left_child
        self.right_child = right_child

    
    def set_left_child(self, condition):
        self.left_child = Conditional_Node(condition)

    def set_right_child(self, condition):
        self.right_child = Conditional_Node(condition)

question = Question_Node(input("Initial Question: "))
condition_1 = input("Condition 1: ")
















print()



