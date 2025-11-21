import customtkinter as ctk
from ui.components import LabeledEntry, IconButton
from logic.calculator import compute_area, pretty_formula
from logic.hints import generate_hints
from logic.progress import save_progress_entry

class TutorScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color='transparent')
        self.router = router
        ctk.CTkLabel(self, text='Tutor', font=('Segoe UI',16,'bold')).pack(anchor='w', pady=(6,4))
        self.shape = ctk.StringVar(value='Square')
        self.shape_menu = ctk.CTkOptionMenu(
            self,
            values=['Square','Rectangle','Triangle'],
            variable=self.shape
        )
        self.shape_menu.pack(pady=6)

        self.d1 = LabeledEntry(self, 'Side / Length / Base:'); self.d1.pack(pady=4)
        self.d2 = LabeledEntry(self, 'Width / Height:'); self.d2.pack(pady=4)
        self.ans = LabeledEntry(self, 'Your computed area:'); self.ans.pack(pady=4)
        btn_frame = ctk.CTkFrame(self, fg_color='transparent'); btn_frame.pack(pady=6)
        IconButton(btn_frame, text='Calculate', command=self.calculate, fg_color='#2B8FE6', text_color='white').pack(side='left', padx=6)
        IconButton(btn_frame, text='Check', command=self.check, fg_color='#7A8FA6').pack(side='left', padx=6)
        IconButton(btn_frame, text='Hint', command=self.hint, fg_color='#7A8FA6').pack(side='left', padx=6)
        self.feedback = ctk.CTkTextbox(self, width=640, height=220); self.feedback.pack(pady=8)
    def calculate(self):
        a=self.d1.get().strip(); b=self.d2.get().strip(); shape=self.shape.get()
        area, _ = compute_area(shape,a,b)
        if area is None:
            self.feedback.insert('end','Enter valid dimensions\n'); return
        self.feedback.insert('end', f'Correct area: {area}\n{pretty_formula(shape,a,b,area)}\n')
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

            # show hints
            for hint in generate_hints(shape, a, b, ans, res['correct_area']):
                self.feedback.insert('end', f"- {hint}\n")

    def hint(self):
        a=self.d1.get().strip(); b=self.d2.get().strip(); area,_=compute_area(self.shape.get(),a,b)
        if area is None: self.feedback.insert('end','Enter dims to get hint\n'); return
        for i,h in enumerate(generate_hints(self.shape.get(),a,b,None,area),start=1): self.feedback.insert('end',f'Step {i}: {h}\n')

    def set_shape(self, shape_name):
        self.shape.set(shape_name)
        self.shape_menu.set(shape_name)  # updates dropdown visually
        self.d1.entry.delete(0, "end")
        self.d2.entry.delete(0, "end")
        self.ans.entry.delete(0, "end")
        self.feedback.delete("1.0", "end")

