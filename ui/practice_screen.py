import customtkinter as ctk
from ui.components import LabeledEntry
from logic.evaluator import grade_answer
from logic.progress import save_progress_entry

class PracticeScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color='transparent')
        self.router = router
        ctk.CTkLabel(self, text='Practice', font=('Segoe UI',16,'bold')).pack(pady=6)
        self.shape = ctk.StringVar(value='Rectangle')
        ctk.CTkOptionMenu(self, values=['Square','Rectangle','Triangle'], variable=self.shape).pack(pady=6)
        self.d1 = LabeledEntry(self,'Dimension 1:'); self.d1.pack(pady=4)
        self.d2 = LabeledEntry(self,'Dimension 2:'); self.d2.pack(pady=4)
        self.ans = LabeledEntry(self,'Your answer:'); self.ans.pack(pady=4)
        ctk.CTkButton(self, text='Load Example', command=self.load_q).pack(pady=6)
        ctk.CTkButton(self, text='Check', command=self.check).pack(pady=6)
        self.feedback = ctk.CTkTextbox(self, width=640, height=200); self.feedback.pack(pady=8)
    def load_q(self):
        if self.shape.get()=='Square': self.d1.set('6'); self.d2.set('')
        if self.shape.get()=='Rectangle': self.d1.set('8'); self.d2.set('3')
        if self.shape.get()=='Triangle': self.d1.set('10'); self.d2.set('4')
        self.feedback.insert('end','Example loaded.\n')
  
    def check(self):
        a = self.d1.get().strip()
        b = self.d2.get().strip()
        ans = self.ans.get().strip()
        shape = self.shape.get()

        from logic.evaluator import grade_answer
        res = grade_answer(shape, a, b, ans)

        if not res.get('ok'):
            self.feedback.insert('end', res.get('message') + '\n')
            return

        self.feedback.insert('end', '\n--- Checking Answer ---\n')

        if res.get('is_correct'):
            self.feedback.insert('end', "✅ Correct!\n")
            save_progress_entry("Student", shape, a, b, ans, res['correct_area'], True)
        else:
            self.feedback.insert('end', f"❌ Not correct.\nCorrect area: {res['correct_area']}\n")
            save_progress_entry("Student", shape, a, b, ans, res['correct_area'], False)

            # Show hints
            for hint in generate_hints(shape, a, b, ans, res['correct_area']):
                self.feedback.insert('end', f"- {hint}\n")

