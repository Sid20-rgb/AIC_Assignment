import customtkinter as ctk
class HomeScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color='transparent')
        self.router = router
        ctk.CTkLabel(self, text='Welcome to Area Tutor', font=('Segoe UI',18,'bold')).pack(pady=16)
        ctk.CTkButton(self, text='Start Tutor', command=lambda: router.show('tutor'), width=200).pack(pady=6)
        ctk.CTkButton(self, text='Practice', command=lambda: router.show('practice'), width=200).pack(pady=6)
        ctk.CTkButton(self, text='Dashboard', command=lambda: router.show('dashboard'), width=200).pack(pady=6)
        ctk.CTkButton(self, text='Quiz', command=lambda: router.show('quiz'), width=200).pack(pady=6)
