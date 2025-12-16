import customtkinter as ctk
from logic.progress import load_progress

class DashboardScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color='transparent')
        self.router = router
        
        ctk.CTkLabel(self, text='Dashboard', font=('Segoe UI', 20, 'bold')).pack(pady=16)

       
        data = load_progress()
        sessions = data.get('sessions', [])
        correct = sum(1 for s in sessions if s.get('result') == 'correct')
        incorrect = sum(1 for s in sessions if s.get('result') != 'correct')

       
        stats_frame = ctk.CTkFrame(self, fg_color='transparent')
        stats_frame.pack(pady=20)

      
        correct_box = ctk.CTkFrame(stats_frame, fg_color="#2EA44F", corner_radius=20)
        correct_box.grid(row=0, column=0, padx=20, pady=10, ipadx=40, ipady=30)  
        ctk.CTkLabel(correct_box, text="Correct", font=('Segoe UI', 18, 'bold'), text_color="white").pack(expand=True)
        ctk.CTkLabel(correct_box, text=str(correct), font=('Segoe UI', 36, 'bold'), text_color="white").pack(expand=True)

        
        incorrect_box = ctk.CTkFrame(stats_frame, fg_color="#D73A49", corner_radius=20)
        incorrect_box.grid(row=0, column=1, padx=20, pady=10, ipadx=40, ipady=30)
        ctk.CTkLabel(incorrect_box, text="Incorrect", font=('Segoe UI', 18, 'bold'), text_color="white").pack(expand=True)
        ctk.CTkLabel(incorrect_box, text=str(incorrect), font=('Segoe UI', 36, 'bold'), text_color="white").pack(expand=True)
