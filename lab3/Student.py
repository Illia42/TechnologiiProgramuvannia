class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self):
        return f"Name = {self.name} ; Phone = {self.phone} ; Email = {self.email} ; Group = {self.group}"

    def to_dict(self):
        """Метод для зручного збереження у CSV"""
        return {
            "student_name": self.name, 
            "mobile": self.phone, 
            "email_addr": self.email, 
            "study_group": self.group
        }