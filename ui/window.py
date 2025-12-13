import os
import customtkinter as ctk
from ui.styles import COLORS, FONTS
from ui.home_screen import HomeScreen
from ui.tutor_screen import TutorScreen
from ui.practice_screen import PracticeScreen
from ui.dashboard_screen import DashboardScreen
from ui.quiz_screen import QuizScreen
from ui.shape_explorer_screen import ShapeExplorerScreen
import tkinter as tk



class Router(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        self.pack(fill='both', expand=True)
        self.screens = {}

    def register(self, name, screen):
        self.screens[name] = screen

    def show(self, name):
        for k, s in self.screens.items():
            s.pack_forget()
        self.screens[name].pack(fill='both', expand=True, padx=12, pady=12)

    def show_tutor(self, shape=None):
        # Navigate to tutor screen
        self.show("tutor")

        # If quiz detected a weak shape → update tutor UI
        tutor_screen = self.screens.get("tutor")
        if shape and tutor_screen:
            tutor_screen.set_shape(shape)


class AreaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shape Smart')
        self.geometry('1000x700')
        self.configure(fg_color=COLORS['bg'])
        
        icon_path = os.path.join(
            os.path.dirname(__file__),
            "..", "assets", "icons", "appLogo.ico"
        )
        self.iconbitmap(icon_path)
          
        # left navigation
        nav = ctk.CTkFrame(self, width=180, fg_color=COLORS['panel'], corner_radius=8)
        nav.pack(side='left', fill='y', padx=12, pady=12)
        btn_home = ctk.CTkButton(nav, text='Home', command=lambda: self.router.show('home')); btn_home.pack(pady=8, padx=10, fill='x')
        btn_tutor = ctk.CTkButton(nav, text='Tutor', command=lambda: self.router.show('tutor')); btn_tutor.pack(pady=8, padx=10, fill='x')
        btn_practice = ctk.CTkButton(nav, text='Practice', command=lambda: self.router.show('practice')); btn_practice.pack(pady=8, padx=10, fill='x')
        btn_dash = ctk.CTkButton(nav, text='Dashboard', command=lambda: self.router.show('dashboard')); btn_dash.pack(pady=8, padx=10, fill='x')
        btn_explorer = ctk.CTkButton(nav, text='Shapes', command=lambda: self.router.show('shape_explorer'))
        btn_explorer.pack(pady=8, padx=10, fill='x')

        # router area
        self.router = Router(self)
        self.router.register('home', HomeScreen(self.router, self.router))
        self.router.register('tutor', TutorScreen(self.router, self.router))
        self.router.register('practice', PracticeScreen(self.router, self.router))
        self.router.register('dashboard', DashboardScreen(self.router, self.router))
        self.router.register('quiz', QuizScreen(self.router, self.router))
        self.router.show('home')
        self.router.register('shape_explorer', ShapeExplorerScreen(self.router, self.router))


def run_app():
    app = AreaApp()
    app.mainloop()
