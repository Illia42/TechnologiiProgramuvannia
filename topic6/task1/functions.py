import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("calc.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def add(a, b):
    res = a + b
    logging.info(f"Виконано додавання: {a} + {b} = {res}")
    return res

def subtract(a, b):
    res = a - b
    logging.info(f"Виконано віднімання: {a} - {b} = {res}")
    return res

def multiply(a, b):
    res = a * b
    logging.info(f"Виконано множення: {a} * {b} = {res}")
    return res

def divide(a, b):
    if b == 0:
        logging.error(f"Спроба ділення на нуль: {a} / {b}")
        return "Division by zero!"
    res = a / b
    logging.info(f"Виконано ділення: {a} / {b} = {res}")
    return res