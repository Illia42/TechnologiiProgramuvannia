
students = [
    {"name": "Олексій", "score": 85},
    {"name": "Анна", "score": 95},
    {"name": "Богдан", "score": 78},
    {"name": "Дар'я", "score": 90}
]


students_by_name = sorted(students, key=lambda student: student["name"])

print("=== Сортування за ім'ям ===")
for s in students_by_name:
    print(s)


students_by_score = sorted(students, key=lambda student: student["score"])

print("\n=== Сортування за оцінкою ===")
for s in students_by_score:
    print(s)