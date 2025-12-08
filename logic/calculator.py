def to_float(v):
    try: return float(v)
    except: return None
def compute_area(shape, d1, d2=''):
    a = to_float(d1)
    b = to_float(d2) if d2 != '' else None

    if shape == 'Square':
        if a is None: return None, 'invalid'
        return round(a*a, 4), f's={a}'
    
    if shape == 'Rectangle':
        if a is None or b is None: return None, 'invalid'
        return round(a*b, 4), f'l={a},w={b}'
    
    if shape == 'Triangle':
        if a is None or b is None: return None, 'invalid'
        return round(0.5*a*b, 4), f'b={a},h={b}'
    
    if shape == 'Circle':
        if a is None: return None, 'invalid'
        area = 3.14159 * a * a
        return round(area, 4), f'r={a}'

    return None, 'invalid'


def pretty_formula(shape, d1, d2, area):
    a = to_float(d1)
    b = to_float(d2) if d2 != '' else None

    if shape == 'Square':
        return f'Area = s × s = {a} × {a} = {area}'
    
    if shape == 'Rectangle':
        return f'Area = l × w = {a} × {b} = {area}'
    
    if shape == 'Triangle':
        return f'Area = 1/2 × b × h = 1/2 × {a} × {b} = {area}'
    
    if shape == 'Circle':
        return f'Area = π × r² = 3.14159 × {a}² = {area}'

    return ''

def compute_perimeter(shape, d1, d2=None, d3=None):

    def to_float(x):
        try: return float(x)
        except: return None

    a = to_float(d1)
    b = to_float(d2)
    # c = to_float(d3)

    if shape == "Square":
        if a is None: return None, None
        return 4 * a, f"P = 4 × {a}"

    if shape == "Rectangle":
        if a is None or b is None: return None, None
        return 2*(a+b), f"P = 2 × ({a} + {b})"

    if shape == "Circle":
        if a is None: return None, None
        import math
        return 2*math.pi*a, f"P = 2π × {a}"

    # if shape == "Triangle":
    #     if a is None or b is None or c is None:
    #         return None, None 
    #     return a+b+c, f"P = {a} + {b} + {c}"
    
    if shape == 'Triangle':
        if a is None or b is None: return None, 'Invalid'
        # Assuming right-angled triangle with base=a, height=b
        import math
        hypotenuse = math.sqrt(a**2 + b**2)
        return round(a + b + hypotenuse, 4), f'b={a},h={b}'   

    return None, None



# def compute_area(shape,d1,d2):
#     a=to_float(d1); b=to_float(d2) if d2!='' else None
#     if shape=='Square':
#         if a is None: return None,'invalid'
#         return round(a*a,4),f's={a}'
#     if shape=='Rectangle':
#         if a is None or b is None: return None,'invalid'
#         return round(a*b,4),f'l={a},w={b}'
#     if shape=='Triangle':
#         if a is None or b is None: return None,'invalid'
#         return round(0.5*a*b,4),f'b={a},h={b}'
#     if shape == "Circle":
#         if not a.isdigit():
#             return None, "Invalid radius"
#         radius = float(a)
#         area = 3.14 * radius * radius
#         return area, None
#     return None,'invalid'
# def pretty_formula(shape,d1,d2,area):
#     if shape=='Square': return f'Area = s × s = {d1} × {d1} = {area}'
#     if shape=='Rectangle': return f'Area = l × w = {d1} × {d2} = {area}'
#     if shape=='Triangle': return f'Area = 1/2 × b × h = 1/2 × {d1} × {d2} = {area}'
#     elif shape == "Circle": return f"Formula: π × r² = 3.14159 × {a}² = {area}"

#     return ''
