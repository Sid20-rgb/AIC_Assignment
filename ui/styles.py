import customtkinter as ctk

# ===== Dark Theme Colors =====
COLORS = {
    'bg': '#0b0f13',        # App background 
    'panel': '#0f1720',     # Panels / frames
    'accent': '#3a86ff',    # Blue accent
    'muted': '#98a0ad',     # Soft gray text
    'success': '#2EA44F',   # Green success
    'danger': '#D73A49'     # Red danger
}


FONTS = {
    'title': ('Segoe UI', 20, 'bold'),
    'header': ('Segoe UI', 12, 'bold'),
    'normal': ('Segoe UI', 11)
}


ctk.set_appearance_mode('dark')


try:
    ctk.set_default_color_theme('dark-blue')
except Exception:
    ctk.set_default_color_theme('blue')
