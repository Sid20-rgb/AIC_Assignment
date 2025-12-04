import customtkinter as ctk
from ui.styles import COLORS, FONTS


SHAPES = {
    "Square": {
        "formula": "A = a²",
        "details": (
            "A square has all sides equal.\n"
            "• Opposite sides are parallel\n"
            "• All angles = 90°\n\n"
            "Real world examples:\n"
            "▪ Chessboard tile\n"
            "▪ Floor tiles\n"
            "▪ Paper sticky notes"
        ),
        "color": "#4FC3F7"
    },
    "Rectangle": {
        "formula": "A = length × width",
        "details": (
            "A rectangle has opposite sides equal.\n"
            "• All angles = 90°\n"
            "• Length is the longest side\n\n"
            "Real world examples:\n"
            "▪ Phone screen\n"
            "▪ Doors\n"
            "▪ Book covers"
        ),
        "color": "#81C784"
    },
    "Triangle": {
        "formula": "A = ½ × base × height",
        "details": (
            "A triangle has 3 sides and 3 angles.\n"
            "• The height is measured perpendicular\n"
            "• Sum of interior angles = 180°\n\n"
            "Real world examples:\n"
            "▪ Road signs\n"
            "▪ Bridge supports\n"
            "▪ Roof structures"
        ),
        "color": "#FFB74D"
    },
    "Circle": {
        "formula": "A = πr²",
        "details": (
            "A circle is defined by its radius (r).\n"
            "• Diameter = 2r\n"
            "• Circumference = 2πr\n\n"
            "Real world examples:\n"
            "▪ Coins\n"
            "▪ Wheels\n"
            "▪ Clock faces"
        ),
        "color": "#E57373"
    }
}


class ShapeExplorerScreen(ctk.CTkFrame):
    def __init__(self, master, router):
        super().__init__(master, fg_color=COLORS["bg"])
        self.router = router
        self.hover_color = "#FFFFFF"

        # ---------- LEFT SIDE SHAPE LIST ----------
        self.left = ctk.CTkFrame(self, width=240, fg_color=COLORS["panel"])
        self.left.pack(side="left", fill="y", padx=10, pady=10)

        lbl = ctk.CTkLabel(self.left, text="Shapes", font=FONTS["title"], text_color="white")
        lbl.pack(pady=(10, 20))

        for shape in SHAPES.keys():
            btn = ctk.CTkButton(
                self.left,
                text=shape,
                fg_color=COLORS["accent"],
                hover_color="#1C7CD6",
                command=lambda s=shape: self.show_shape(s)
            )
            btn.pack(pady=6, padx=12, fill="x")

        # ---------- RIGHT SIDE CONTENT ----------
        self.right = ctk.CTkFrame(self, fg_color=COLORS["panel"])
        self.right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.title_label = ctk.CTkLabel(self.right, text="", font=FONTS["title"], text_color="white")
        self.title_label.pack(pady=10)

        self.canvas = ctk.CTkCanvas(self.right, width=350, height=260, bg=COLORS["panel"], highlightthickness=0)
        self.canvas.pack(pady=10)

        self.formula_label = ctk.CTkLabel(self.right, text="", font=FONTS["header"], text_color=COLORS["accent"])
        self.formula_label.pack(pady=10)

        self.details_label = ctk.CTkLabel(
            self.right,
            text="",
            font=FONTS["normal"],
            text_color="white",
            justify="left",
            wraplength=450
        )
        self.details_label.pack(pady=10)

        # For hover interactions
        self.canvas.bind("<Enter>", self.on_hover)
        self.canvas.bind("<Leave>", self.end_hover)

        self.current_shape = None
        self.hover_active = False


    # ---------- HOVER EFFECT ----------
    def on_hover(self, event):
        self.hover_active = True
        self.redraw_shape(glow=True)

    def end_hover(self, event):
        self.hover_active = False
        self.redraw_shape(glow=False)


    # ---------- DRAW SHAPE ----------
    def redraw_shape(self, glow=False):
        if not self.current_shape:
            return

        shape = self.current_shape
        base_color = SHAPES[shape]["color"]

        # Lighter fill colors (valid Tkinter hex)
        fill_colors = {
            "Square": "#B3E5FC",
            "Rectangle": "#C8E6C9",
            "Triangle": "#FFE0B2",
            "Circle": "#FFCDD2"
        }

        fill = fill_colors.get(shape, base_color)
        stroke = 5 if glow else 3

        self.canvas.delete("all")

        if shape == "Square":
            self.canvas.create_rectangle(
                80, 40, 250, 210,
                outline=base_color,
                width=stroke,
                fill=fill
            )

        elif shape == "Rectangle":
            self.canvas.create_rectangle(
                70, 70, 280, 200,
                outline=base_color,
                width=stroke,
                fill=fill
            )

        elif shape == "Triangle":
            self.canvas.create_polygon(
                100, 200,
                200, 50,
                300, 200,
                outline=base_color,
                width=stroke,
                fill=fill
            )

        elif shape == "Circle":
            self.canvas.create_oval(
                70, 40,
                270, 240,
                outline=base_color,
                width=stroke,
                fill=fill
            )


    # ---------- UPDATE SHAPE INFO ----------
    def show_shape(self, shape):
        self.current_shape = shape

        info = SHAPES[shape]

        self.title_label.configure(text=shape)
        self.formula_label.configure(text="Formula: " + info["formula"])
        self.details_label.configure(text=info["details"])

        self.redraw_shape(glow=False)
