from calculator_oop import Calculator

def main():
    
    calc = Calculator()
    
    print("=== ООП Калькулятор ===")
    
    while True:
        op = input("Введіть оператор (+, -, *, /) або 'exit' для виходу: ")
        
        if op == "exit":
            print("Роботу завершено!")
            break
            
        if op not in ['+', '-', '*', '/']:
            print("Некоректний оператор!")
            continue
            
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка! Потрібно вводити числа.")
            continue
            
        if op == '+':
            print("Результат:", calc.add(a, b))
        elif op == '-':
            print("Результат:", calc.subtract(a, b))
        elif op == '*':
            print("Результат:", calc.multiply(a, b))
        elif op == '/':
            print("Результат:", calc.divide(a, b))

if __name__ == "__main__":
    main()