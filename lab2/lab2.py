
import csv
from sys import argv

phonebook_db = []

def loadData(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                phonebook_db.append({
                    "student_name": row["student_name"],
                    "mobile": row["mobile"],
                    "email_addr": row["email_addr"],
                    "study_group": row["study_group"]
                })
        print(f"Data loaded from {file_name}")
    except FileNotFoundError:
        print("File not found. Starting with an empty phonebook.")

def saveData(file_name):
    with open(file_name, "w", newline='', encoding="utf-8") as file:
        fieldnames = ["student_name", "mobile", "email_addr", "study_group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in phonebook_db:
            writer.writerow(record)
    print(f"Data saved to {file_name}")

def printAllList():
    for record in phonebook_db:
        output_str = "Name = " + record["student_name"] + " ; Phone = " + record["mobile"] + " ; Email = " + record["email_addr"] + " ; Group = " + record["study_group"]
        print(output_str)
    return

def insert_record(name, phone, email, group):
    new_entry = {"student_name": name, "mobile": phone, "email_addr": email, "study_group": group}
    target_pos = 0

    for entry in phonebook_db:
        if name > entry["student_name"]:
            target_pos += 1
        else:
            break
    phonebook_db.insert(target_pos, new_entry)

def remove_record(name):
    remove_index = -1
    for entry in phonebook_db:
        if name == entry["student_name"]:
            remove_index = phonebook_db.index(entry)
            break
            
    if remove_index != -1:
        del phonebook_db[remove_index]
        return True
    return False
 

def addNewElement():
    s_name = input("Please enter student name: ")
    s_phone = input("Please enter student phone: ")
    s_email = input("Please enter student email: ")
    s_group = input("Please enter student group: ")
    
    insert_record(s_name, s_phone, s_email, s_group)
    print("New element has been added")
    return

def deleteElement():
    name_to_remove = input("Please enter name to be deleted: ")
    
    if remove_record(name_to_remove):
        print("Element deleted successfully")
    else:
        print("Element was not found")
    return

def editStudent():
    name_to_edit = input("Please enter name to be updated: ")
    
    if remove_record(name_to_edit):
        print("Enter new info:")
        updated_name = input("Please enter student name: ")
        updated_phone = input("Please enter student phone: ")
        updated_email = input("Please enter student email: ")
        updated_group = input("Please enter student group: ")
        
        insert_record(updated_name, updated_phone, updated_email, updated_group)
        print("Data updated. Sorting applied.")
    else:
        print("Element was not found")
    return

def main():
    if len(argv) < 2:
        print("Please provide the CSV filename. Example: python lab2.py lab2.csv")
        return
        
    file_name = argv[1]
    loadData(file_name)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                editStudent()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                saveData(file_name)
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()