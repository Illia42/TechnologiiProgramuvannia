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

if op == "+":
    res = add(a, b)
elif op == "-":
    res = subtract(a, b)
elif op == "*":
    res = multiply(a, b)
elif op == "/":
    res = divide(a, b)
else:
    res = "Unknown operation"

print("Result:", res)