class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name:<10} | Вік: {self.age}"

students = [
    Student("Олексій", 21),
    Student("Анна", 19),
    Student("Богдан", 22),
    Student("Дар'я", 18)
]

sorted_students = sorted(students, key=lambda student: student.age)

print("=== Відсортований список студентів за віком ===")
for student in sorted_students:
    print(student)