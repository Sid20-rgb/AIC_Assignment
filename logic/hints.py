def generate_hints(shape,d1,d2,student_ans,correct_area):
    hints=[]
    try: a=float(d1)
    except: a=None
    try: b=float(d2) if d2!='' else None
    except: b=None
    if shape=='Triangle': hints.append('Remember: 1/2 × base × height.')
    else: hints.append('Multiply the two dimensions.')
    if student_ans is not None:
        try:
            s=float(student_ans)
            if a is not None and b is not None and abs(s-(a+b))<abs(s-correct_area):
                hints.append('You may have added instead of multiplied.')
        except: pass
    hints.append('Work step-by-step: identify dims → substitute → compute.')
    return hints
