class QuizBrain():
    def __init__(self, question_number, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.next_question(question_number,question_list)

    def next_question(self,question_number, question_list):
        points_right = 0
        points_wrong = 0
        while question_number <= 11:
            guess = input((f"Q.{question_number+1} {question_list[question_number].text} True or False?"))
            if guess == question_list[question_number].answer:
                points_right+=1
            else:points_wrong+=1
            question_number +=1
        print(f"You finished, your score was {points_right}/{points_wrong}")
                



    