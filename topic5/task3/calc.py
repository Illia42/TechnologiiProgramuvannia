import functions
import operations

while True:
    op = operations.get_operator()
    
    if op == "exit":
        print("Goodbye!")
        break
        
    a = operations.get_number("Enter first number: ")
    b = operations.get_number("Enter second number: ")
    
    if op == "+":
        print("Result:", functions.add(a, b))
    elif op == "-":
        print("Result:", functions.subtract(a, b))
    elif op == "*":
        print("Result:", functions.multiply(a, b))
    elif op == "/":
        print("Result:", functions.divide(a, b))
    else:
        print("Invalid operator!")