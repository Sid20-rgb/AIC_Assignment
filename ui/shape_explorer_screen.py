import customtkinter as ctk
from ui.styles import COLORS, FONTS
from ontology.ontology_loader import OntologyLoader


OWL_PATH = "ontology/its_shape.owl"


SHAPES = {
    "Square": {
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
        self.onto = OntologyLoader(OWL_PATH)

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

        
        self.operation_var = ctk.StringVar(value="Area")
        self.operation_menu = ctk.CTkOptionMenu(
            self.right,
            values=["Area", "Perimeter"],
            variable=self.operation_var,
            fg_color="#1E88E5",
            command=self.update_formula
        )
        self.operation_menu.pack(pady=5)

        self.details_label = ctk.CTkLabel(
            self.right,
            text="",
            font=FONTS["normal"],
            text_color="white",
            justify="left",
            wraplength=450
        )
        self.details_label.pack(pady=10)

     
        self.canvas.bind("<Enter>", self.on_hover)
        self.canvas.bind("<Leave>", self.end_hover)

        self.current_shape = None
        self.hover_active = False


    def on_hover(self, event):
        self.hover_active = True
        self.redraw_shape(glow=True)

    def end_hover(self, event):
        self.hover_active = False
        self.redraw_shape(glow=False)

 
    def redraw_shape(self, glow=False):
        if not self.current_shape:
            return

        shape = self.current_shape
        base_color = SHAPES[shape]["color"]

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
            self.canvas.create_rectangle(80, 40, 250, 210, outline=base_color, width=stroke, fill=fill)

        elif shape == "Rectangle":
            self.canvas.create_rectangle(70, 70, 280, 200, outline=base_color, width=stroke, fill=fill)

        elif shape == "Triangle":
            self.canvas.create_polygon(100, 200, 200, 50, 300, 200, outline=base_color, width=stroke, fill=fill)

        elif shape == "Circle":
            self.canvas.create_oval(70, 40, 270, 240, outline=base_color, width=stroke, fill=fill)

    # ---------- Dynamic Formula Update (OWL) ----------
    def update_formula(self, *args):
        if not self.current_shape:
            return

        op = self.operation_var.get()
        formula = self.onto.get_formula(self.current_shape, op)
        self.formula_label.configure(text=f"{op} Formula: {formula}")

    
    def show_shape(self, shape):
        self.current_shape = shape

        info = SHAPES[shape]

        self.title_label.configure(text=shape)
        self.details_label.configure(text=info["details"])

       
        self.update_formula()

        self.redraw_shape(glow=False)
