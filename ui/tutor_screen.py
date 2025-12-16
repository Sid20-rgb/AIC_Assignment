import customtkinter as ctk
from ui.components import LabeledEntry, IconButton
from logic.calculator import compute_area, compute_perimeter, pretty_formula
from logic.hints import generate_hints
from logic.progress import save_progress_entry

class TutorScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color='transparent')
        self.router = router

        ctk.CTkLabel(self, text='Tutor', font=('Segoe UI',16,'bold')).pack(anchor='w', pady=(6,4))

        
        self.shape = ctk.StringVar(value='Square')
        self.shape_menu = ctk.CTkOptionMenu(
            self, values=['Square','Rectangle','Triangle','Circle'],
            variable=self.shape,
            command=self.on_shape_change
        )
        self.shape_menu.pack(pady=6)

       
        self.calc_type = ctk.StringVar(value='Area')
        self.calc_menu = ctk.CTkOptionMenu(
            self,
            values=['Area','Perimeter'],
            variable=self.calc_type
        )
        self.calc_menu.pack(pady=6)
        
      
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=10)

        self.d1 = LabeledEntry(self.input_frame, 'Side / Length / Base:')
        self.d1.grid(row=0, column=0, pady=6)

        self.d2 = LabeledEntry(self.input_frame, 'Width / Height:')
        self.d2.grid(row=1, column=0, pady=6)

        self.d3 = LabeledEntry(self.input_frame, 'Side C:')
        self.d3.grid(row=2, column=0, pady=6)
        self.d3.grid_remove()   


        self.ans = LabeledEntry(self.input_frame, 'Your computed area/perimeter:')
        self.ans.grid(row=3, column=0, pady=6)

        btn_frame = ctk.CTkFrame(self, fg_color='transparent')
        btn_frame.pack(pady=6)
        IconButton(btn_frame, text='Calculate', command=self.calculate,
                   fg_color='#2B8FE6', text_color='white').pack(side='left', padx=6)
        IconButton(btn_frame, text='Check', command=self.check,
                   fg_color='#7A8FA6').pack(side='left', padx=6)
        IconButton(btn_frame, text='Hint', command=self.hint,
                   fg_color='#7A8FA6').pack(side='left', padx=6)

        self.feedback = ctk.CTkTextbox(self, width=640, height=220)
        self.feedback.pack(pady=8)

        # Initial layout update
        self.update_fields("Square")

    
    def on_shape_change(self, value):
        self.update_fields(value)

    def update_fields(self, shape):
        """Update visible fields depending on chosen shape, using GRID."""
        calc_type = self.calc_type.get()

      
        self.d1.label.configure(text="Side / Length / Base:")
        self.d2.label.configure(text="Width / Height:")
        self.d3.grid_remove()
        if shape == "Circle":
            self.d1.label.configure(text="Radius:")
            self.d2.grid_remove()     
        else:
            self.d1.label.configure(text="Side / Length / Base:")
            self.d2.grid()         

    
        self.d1.entry.delete(0, "end")
        self.d2.entry.delete(0, "end")
        self.ans.entry.delete(0, "end")
        self.feedback.delete("1.0", "end")

  
    def calculate(self):
        shape = self.shape.get()
        a = self.d1.get().strip()
        b = self.d2.get().strip()
        if self.calc_type.get() == 'Area':
            value, formula = compute_area(shape, a, b)
        else:
            value, formula = compute_perimeter(shape, a, b)

        if value is None:
            self.feedback.insert('end', 'Enter valid dimensions\n')
            return

        if formula:
            self.feedback.insert('end', f"{self.calc_type.get()}: {value}\n{formula}\n")
        else:
            self.feedback.insert('end', f"{self.calc_type.get()}: {value}\n")



    def check(self):
        a = self.d1.get().strip()
        b = self.d2.get().strip()
        ans = self.ans.get().strip()
        shape = self.shape.get()

        from logic.evaluator import grade_answer

     
        calc_type = self.calc_type.get()

        if calc_type == "Area":
            correct_value, _ = compute_area(shape, a, b)
        else:
            correct_value, _ = compute_perimeter(shape, a, b)

        if correct_value is None:
            self.feedback.insert('end', "Enter valid dimensions\n")
            return

     
        try:
            student_val = float(ans)
            is_correct = abs(student_val - correct_value) < 0.0001
        except:
            is_correct = False

        self.feedback.insert('end', '\n--- Checking Answer ---\n')

        if is_correct:
            self.feedback.insert('end', "✅ Correct!\n")
        else:
            self.feedback.insert('end', f"❌ Not correct.\nCorrect {calc_type.lower()}: {correct_value}\n")

           
            hints = generate_hints(shape, a, b, ans, correct_value, calc_type)

            for i, hint in enumerate(hints, start=1):
                self.feedback.insert("end", f"Step {i}: {hint}\n")



    def hint(self):
        a = self.d1.get().strip()
        b = self.d2.get().strip()
        shape = self.shape.get()
        calc_type = self.calc_type.get()

    
        if calc_type == "Area":
            correct_value, _ = compute_area(shape, a, b)
        else:
            correct_value, _ = compute_perimeter(shape, a, b)

        if correct_value is None:
            self.feedback.insert("end", "Enter dimensions to get a hint\n")
            return

        hints = generate_hints(shape, a, b, None, correct_value, calc_type)

        for i, h in enumerate(hints, start=1):
            self.feedback.insert("end", f"Step {i}: {h}\n")




    def set_shape(self, shape_name):
        self.shape.set(shape_name)
        self.shape_menu.set(shape_name)
        self.update_fields(shape_name)
