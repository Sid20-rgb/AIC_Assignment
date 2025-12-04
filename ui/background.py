import customtkinter as ctk
from PIL import Image

class BackgroundMixin:
    _bg_loaded = False  # prevents double-loading

    def load_background(self, image_path):
        self._bg_image_path = image_path
        self.bind("<Map>", self._load_bg_once)  # load when widget is mapped

    def _load_bg_once(self, event=None):
        if self._bg_loaded: 
            return
        self._bg_loaded = True

        # Real background loading happens HERE
        self._bg_image_pil = Image.open(self._bg_image_path)
        self._bg_image = ctk.CTkImage(self._bg_image_pil, size=(1400, 900))

        self.bg_label = ctk.CTkLabel(self, text="", image=self._bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()
