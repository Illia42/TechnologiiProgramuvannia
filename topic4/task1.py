def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    op = input("Enter operator (+, -, *, /) or 'exit': ")

    if op.lower() == "exit":
        print("Goodbye!")
        break

    if op not in ("+", "-", "*", "/"):
        print("Invalid operator!")
        continue

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", subtract(a, b))
    elif op == "*":
        print("Result:", multiply(a, b))
    elif op == "/":
        print("Result:", divide(a, b))