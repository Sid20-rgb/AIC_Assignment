import customtkinter as ctk
from ui.splash_screen import SplashScreen
from ui.window import run_app


def start_app():
    run_app()


if __name__ == '__main__':
    root = ctk.CTk()
    root.withdraw()

    SplashScreen(root, on_finish=start_app, logo_path="logo.png")

    root.mainloop()
