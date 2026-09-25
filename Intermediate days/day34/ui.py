from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_Ui:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.question = "Blah blah blah"

        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF")
        self.question_text = self.canvas.create_text(150, 125, width=200, text=self.question,font=("Arial", 20, "italic"))
        self.canvas.grid(columnspan=2, row=1, pady=50)

        self.score_label = Label(text=f"Score: {self.score}", padx=20, pady=20, background=THEME_COLOR, foreground="#FFFFFF")
        self.score_label.grid(row=0, column=1)
        
        self.img_true = PhotoImage(file="Intermediate days\\day34\\images\\true.png")
        self.img_false = PhotoImage(file="Intermediate days\\day34\\images\\false.png")
        self.rightB = Button(image=self.img_true, highlightthickness=0, command=self.true)
        self.wrongB = Button(image=self.img_false, highlightthickness=0, command=self.false)
        self.rightB.grid(row=2, column=0,)
        self.wrongB.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def true(self):
        self.feedback(self.quiz.check_answer("True"))
        
    def false(self):
        self.feedback(self.quiz.check_answer("False"))

    def get_next_question(self):
        self.canvas.config(background="#FFFFFF")
        if self.quiz.still_has_questions():
            self.score_label.config(text=F"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end")
            self.rightB.config(state="disabled")
            self.wrongB.config(state="disabled")

    def feedback(self, is_right):
        if is_right == True: 
            self.score += 1
            self.canvas.config(background="#81DBAE")
        else: 
            self.canvas.config(background="#FA4335")
        self.window.after(1000, self.get_next_question)
       
 