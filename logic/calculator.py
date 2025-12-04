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
