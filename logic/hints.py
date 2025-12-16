def generate_hints(shape, d1, d2, student_ans, correct_value, calc_type="Area"):
    hints = []

    try: a = float(d1)
    except: a = None
    try: b = float(d2) if d2 != '' else None
    except: b = None

    if calc_type == "Area":
        if shape == 'Triangle': 
            hints.append('Remember: 1/2 × base × height.')
        elif shape == "Circle":
            hints.extend([
                "Area of a circle is π × r².",
                f"Square the radius: {a}² = {a**2 if a else '?'}",
                f"Multiply by π (3.14159).",
                f"Final area ≈ {correct_value}"
            ])
        else:
            hints.append('Multiply the two dimensions.')

        # Common area mistake hint
        if student_ans is not None:
            try:
                s = float(student_ans)
                if a is not None and b is not None and abs(s - (a+b)) < abs(s - correct_value):
                    hints.append('You may have added instead of multiplied.')
            except: pass

    elif calc_type == "Perimeter":
        if shape == 'Square':
            hints.append('Perimeter = 4 × side.')
        elif shape == 'Rectangle':
            hints.append('Perimeter = 2 × (length + width).')
        elif shape == 'Triangle':
            hints.append('Perimeter = sum of all three sides (base + height + ...).')
        elif shape == 'Circle':
            hints.extend([
                "Perimeter (circumference) of a circle = 2 × π × r.",
                f"Multiply radius by 2 × π (3.14159).",
                f"Final perimeter ≈ {correct_value}"
            ])

        # Optional: check for addition vs multiplication mistakes
        if student_ans is not None:
            try:
                s = float(student_ans)
                if a is not None and b is not None and abs(s - (a*b)) < abs(s - correct_value):
                    hints.append('You may have multiplied instead of adding for perimeter.')
            except: pass

    hints.append('Work step-by-step: identify dims → substitute → compute.')
    return hints
