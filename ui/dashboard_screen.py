import customtkinter as ctk
from logic.progress import load_progress
class DashboardScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color='transparent')
        self.router = router
        ctk.CTkLabel(self, text='Dashboard', font=('Segoe UI',16,'bold')).pack(pady=6)
        data = load_progress()
        sessions = data.get('sessions', [])
        correct = sum(1 for s in sessions if s.get('result')=='correct')
        incorrect = sum(1 for s in sessions if s.get('result')!='correct')
        ctk.CTkLabel(self, text=f'Correct: {correct}   Incorrect: {incorrect}').pack(pady=8)
