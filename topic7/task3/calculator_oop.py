class Calculator:
    """Клас для виконання базових математичних операцій."""
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Помилка: ділення на нуль!"
        return a / b