from sys import argv
from Student import Student
from StudentList import StudentList
from Utils import Utils

def add_new_element(student_list):
    s_name = input("Please enter student name: ")
    s_phone = input("Please enter student phone: ")
    s_email = input("Please enter student email: ")
    s_group = input("Please enter student group: ")
    student = Student(s_name, s_phone, s_email, s_group)
    student_list.insert(student)
    print("New element has been added")

def delete_element(student_list):
    name_to_remove = input("Please enter name to be deleted: ")
    if student_list.remove(name_to_remove):
        print("Element deleted successfully")
    else:
        print("Element was not found")

def edit_student(student_list):
    name_to_edit = input("Please enter name to be updated: ")
    print("Enter new info:")
    updated_name = input("Please enter student name: ")
    updated_phone = input("Please enter student phone: ")
    updated_email = input("Please enter student email: ")
    updated_group = input("Please enter student group: ")
    
    new_student = Student(updated_name, updated_phone, updated_email, updated_group)
    if student_list.update(name_to_edit, new_student):
        print("Data updated. Sorting applied.")
    else:
        print("Element was not found")

def main():
    if len(argv) < 2:
        print("Please provide the CSV filename. Example: python main.py lab3.csv")
        return
        
    file_name = argv[1]
    
    
    directory = StudentList()
    Utils.load_data(file_name, directory)
    
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ").upper()
        
        if choice == "C":
            print("New element will be created:")
            add_new_element(directory)
            directory.print_all()
        elif choice == "U":
            print("Existing element will be updated")
            edit_student(directory)
            directory.print_all()
        elif choice == "D":
            print("Element will be deleted")
            delete_element(directory)
            directory.print_all()
        elif choice == "P":
            print("List will be printed")
            directory.print_all()
        elif choice == "X":
            print("Exit()")
            Utils.save_data(file_name, directory)
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()