import logging

def get_number(text):
    while True:
        try:
            val = float(input(text))
            logging.info(f"Введено число: {val}")
            return val
        except ValueError:
            logging.warning("Користувач ввів некоректні дані замість числа!")
            print("Помилка! Введіть дійсне число.")

def get_operator():
    op = input("Enter operator (+, -, *, /) or 'exit': ")
    logging.info(f"Обрана операція/команда: '{op}'")
    return op