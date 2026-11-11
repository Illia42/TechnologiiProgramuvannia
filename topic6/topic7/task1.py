class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Користувач: {self.name}, Вік: {self.age}"

person1 = Person("Іван", 20)

print(person1)