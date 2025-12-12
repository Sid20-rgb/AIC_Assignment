import customtkinter as ctk
from PIL import Image, ImageTk

class SplashScreen(ctk.CTkToplevel):
    def __init__(self, parent, on_finish, logo_path="logo.png"):
        super().__init__(parent)

        self.on_finish = on_finish

        # Window: borderless and centered
        self.overrideredirect(True)
        w, h = 450, 320
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

        ctk.set_appearance_mode("dark")

        # Background frame
        frame = ctk.CTkFrame(self, fg_color="#0a0a0a", corner_radius=12)
        frame.pack(fill="both", expand=True)

        # -------------------------------
        # LOGO IMAGE
        # -------------------------------
        try:
            img = Image.open(logo_path)
            img = img.resize((160, 160))
            self.logo = ImageTk.PhotoImage(img)

            image_label = ctk.CTkLabel(frame, text="", image=self.logo)
            image_label.pack(pady=10)
        except:
            # fallback text if image is missing
            ctk.CTkLabel(frame, text="ITS Shape Smart",
                         font=("Segoe UI", 22, "bold")).pack(pady=12)

        # APP TITLE
        ctk.CTkLabel(
            frame,
            text="Loading, please wait...",
            font=("Segoe UI", 16)
        ).pack(pady=8)

        # Progress Bar
        self.progress = ctk.CTkProgressBar(frame, width=260)
        self.progress.pack(pady=20)
        self.progress.set(0)
        self.progress_val = 0

        # Start progress animation
        self.animate_progress()

    def animate_progress(self):
        if self.progress_val < 1:
            self.progress_val += 0.02
            self.progress.set(self.progress_val)
            self.after(60, self.animate_progress)
        else:
            self.destroy()
            self.on_finish()
