import customtkinter as ctk

class HomeScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color='transparent')
        self.router = router
        
       
        ctk.CTkLabel(self, text='Welcome to Shape Smart',
                     font=('Segoe UI', 30, 'bold')).pack(pady=16)
        
       
        btn_frame = ctk.CTkFrame(self, fg_color='transparent')
        btn_frame.pack(pady=20)

    
        button_font = ('Segoe UI', 18)
        button_width = 200
        button_height = 200
        button_corner_radius = 20  

      
        buttons = [
            ("Start Tutor", lambda: router.show('tutor')),
            ("Practice", lambda: router.show('practice')),
            ("Dashboard", lambda: router.show('dashboard')),
            ("Quiz", lambda: router.show('quiz'))
        ]

        
        for idx, (text, cmd) in enumerate(buttons):
            row = idx // 2
            col = idx % 2
            ctk.CTkButton(
                btn_frame,
                text=text,
                command=cmd,
                width=button_width,
                height=button_height,
                font=button_font,
                corner_radius=button_corner_radius
            ).grid(row=row, column=col, padx=20, pady=20)
