from logic.calculator import compute_area
def grade_answer(shape,d1,d2,student_ans):
    try:
        correct,_=compute_area(shape,d1,d2)
        if correct is None: return {'ok':False,'message':'Invalid dimensions'}
        student=float(student_ans)
    except Exception:
        return {'ok':False,'message':'Invalid student answer'}
    tol=max(0.01,abs(correct)*0.02)
    return {'ok':True,'is_correct': abs(student-correct)<=tol, 'correct_area':correct, 'tolerance':tol}
