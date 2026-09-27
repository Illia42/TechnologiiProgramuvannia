def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

match op:
    case "+":
        res = add(a, b)
    case "-":
        res = subtract(a, b)
    case "*":
        res = multiply(a, b)
    case "/":
        res = divide(a, b)
    case _:
        res = "Unknown operation"

print("Result:", res)