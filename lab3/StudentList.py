from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def insert(self, student):
        """Додавання студента зі збереженням алфавітного сортування за ім'ям"""
        target_pos = 0
        for entry in self.students:
            if student.name > entry.name:
                target_pos += 1
            else:
                break
        self.students.insert(target_pos, student)

    def remove(self, name):
        """Видалення студента за ім'ям"""
        for i, student in enumerate(self.students):
            if student.name == name:
                del self.students[i]
                return True
        return False

    def update(self, old_name, new_student):
        """Оновлення даних (видалення старого + додавання нового)"""
        if self.remove(old_name):
            self.insert(new_student)
            return True
        return False

    def print_all(self):
        """Виведення всіх студентів"""
        if not self.students:
            print("List is empty.")
        for student in self.students:
            print(student)

    def clear(self):
        """Очищення списку (для тестів)"""
        self.students = []