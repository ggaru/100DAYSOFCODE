from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
questions = []


for i in range(0, len(question_data)):
        questions.append(Question(question_data[i]["text"],question_data[i]["answer"]))
quest = QuizBrain(0, questions)





