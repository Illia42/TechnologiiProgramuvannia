import math

def calculate_d(a, b, c):
    return b * b - 4 * a * c

def find_roots(a, b, c):
    if a == 0:
        return "Not a quadratic equation"

    d = calculate_d(a, b, c)

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1, root2
    elif d == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No roots"

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

ans = find_roots(a, b, c)
print("Answer:", ans)