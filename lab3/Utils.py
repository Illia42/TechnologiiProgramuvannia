import csv
from Student import Student

class Utils:
    @staticmethod
    def load_data(file_name, student_list):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row["student_name"], 
                        row["mobile"], 
                        row["email_addr"], 
                        row["study_group"]
                    )
                    student_list.insert(student)
            print(f"Data loaded from {file_name}")
        except FileNotFoundError:
            print("File not found. Starting with an empty phonebook.")

    @staticmethod
    def save_data(file_name, student_list):
        with open(file_name, "w", newline='', encoding="utf-8") as file:
            fieldnames = ["student_name", "mobile", "email_addr", "study_group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list.students:
                writer.writerow(student.to_dict())
        print(f"Data saved to {file_name}")