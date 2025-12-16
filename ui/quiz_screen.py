import json

import customtkinter as ctk

from logic.evaluator import grade_answer
from logic.progress import save_progress_entry


class QuizScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color="transparent")
        self.router = router

        with open("data/quiz_questions.json") as f:
            self.questions = json.load(f)

        self.current_shape = ctk.StringVar(value="Square")
        self.index = 0

        ctk.CTkLabel(self, text="Quiz", font=("Segoe UI",18,"bold")).pack(pady=6)

        ctk.CTkOptionMenu(self, values=list(self.questions.keys()), variable=self.current_shape,
                          command=lambda v: self.reset_quiz()).pack()

        self.question_label = ctk.CTkLabel(self, text="", font=("Segoe UI",14))
        self.question_label.pack(pady=10)

        self.answer_entry = ctk.CTkEntry(self)
        self.answer_entry.pack(pady=6)

        ctk.CTkButton(self, text="Submit", command=self.submit).pack(pady=6)

        self.feedback = ctk.CTkTextbox(self, width=600, height=250)
        self.feedback.pack(pady=6)

        self.reset_quiz()

    def reset_quiz(self):
        self.index = 0
        self.answers_correct = {shape: 0 for shape in self.questions}
        self.total_questions = {shape: len(self.questions[shape]) for shape in self.questions}
        self.load_question()

    def load_question(self):
        shape = self.current_shape.get()
        q = self.questions[shape][self.index]
        self.question_label.configure(text=q["question"])

    def submit(self):
        shape = self.current_shape.get()

       
        if self.index >= len(self.questions[shape]):
            return

        q = self.questions[shape][self.index]
        user_ans = self.answer_entry.get().strip()

        res = grade_answer(shape, q["a"], q.get("b"), user_ans)

        if res.get('is_correct'):
            self.answers_correct[shape] += 1
            self.feedback.insert("end", "✅ Correct!\n")
        else:
            self.feedback.insert("end", "❌ Incorrect.\n")

        self.index += 1

     
        if self.index >= len(self.questions[shape]):
            self.feedback.insert("end", "\n=== Quiz Finished ===\n")
            weak_shape = self.detect_weak_shape()
            if weak_shape:
                self.feedback.insert("end", f"⚠ You need help with **{weak_shape}**.\n")
                self.router.show_tutor(shape=weak_shape)
            return

        self.load_question()

    def detect_weak_shape(self):
        accuracy = {
            shape: self.answers_correct[shape] / self.total_questions[shape]
            for shape in self.questions
        }
        weak = min(accuracy, key=accuracy.get)
        if accuracy[weak] < 0.7:
            return weak
        return None
    
    def show_tutor(self, shape=None):
        frame = self.frames["Tutor"]  

        if shape is not None:
        
            frame.shape.set(shape)

        self.show_frame("Tutor")


