
import cmath

def solve_cubic(a, b, c, d):
    discrim = b**2 - 4*a*c
    if discrim < 0:
        
        root1 = (-b + cmath.sqrt(discrim)) / (2*a)
        root2 = (-b - cmath.sqrt(discrim)) / (2*a)
        root3 = (-b + cmath.sqrt(abs(discrim))) / (2*a)
        return root1, root2, root3
    elif discrim == 0:
        
        root1 = -b / (2*a)
        root2 = -b / (2*a)
        root3 = -b / (2*a)
        return root1, root2, root3
    else:
        
        root1 = (-b + discrim**0.5) / (2*a)
        root2 = (-b - discrim**0.5) / (2*a)
        root3 = (-b + discrim**0.5) / (2*a)
        return root1, root2, root3


a = 1
b = -6
c = 11
d = -6
roots = solve_cubic(a, b, c, d)
print(roots)