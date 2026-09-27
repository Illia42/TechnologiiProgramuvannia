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

while True:
    op = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
    
    if op == "exit":
        print("Goodbye!")
        break

    if op not in ("+", "-", "*", "/"):
        print("Invalid operation!")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    match op:
        case "+":
            print("Result:", add(a, b))
        case "-":
            print("Result:", subtract(a, b))
        case "*":
            print("Result:", multiply(a, b))
        case "/":
            print("Result:", divide(a, b))