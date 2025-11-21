import customtkinter as ctk
from tkinter import PhotoImage

class LabeledEntry(ctk.CTkFrame):
    def __init__(self, master, label, width=180):
        super().__init__(master, fg_color='transparent')
        self.label = ctk.CTkLabel(self, text=label)
        self.entry = ctk.CTkEntry(self, width=width)
        self.label.pack(anchor='w', padx=6, pady=(2,0))
        self.entry.pack(anchor='w', padx=6, pady=(2,6))
    def get(self): return self.entry.get()
    def set(self, v):
        self.entry.delete(0,'end'); self.entry.insert(0,str(v))

class IconButton(ctk.CTkButton):
    def __init__(self, master, text, icon_path=None, **kwargs):
        super().__init__(master, text=text, **kwargs)
        if icon_path:
            try:
                img = PhotoImage(file=icon_path)
                self.configure(image=img, compound='left')
                self._img = img
            except Exception:
                pass
