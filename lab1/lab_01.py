phonebook_db = [
    {"student_name": "Andriy", "mobile": "0991234567", "email_addr": "andriy@mail.com", "study_group": "KB-251"},
    {"student_name": "Ivan", "mobile": "0667654321", "email_addr": "ivan@mail.com", "study_group": "KB-252"},
    {"student_name": "Oksana", "mobile": "0501112233", "email_addr": "oksana@mail.com", "study_group": "KB-251"},
    {"student_name": "Yulia", "mobile": "0679998877", "email_addr": "yulia@mail.com", "study_group": "KB-252"}
]

def printAllList():
    for record in phonebook_db:
        output_str = "Name = " + record["student_name"] + " ; Phone = " + record["mobile"] + " ; Email = " + record["email_addr"] + " ; Group = " + record["study_group"]
        print(output_str)
    return

def addNewElement():
    s_name = input("Please enter student name: ")
    s_phone = input("Please enter student phone: ")
    s_email = input("Please enter student email: ")
    s_group = input("Please enter student group: ")
    
    new_entry = {"student_name": s_name, "mobile": s_phone, "email_addr": s_email, "study_group": s_group}
    
    target_pos = 0
    for entry in phonebook_db:
        if s_name > entry["student_name"]:
            target_pos += 1
        else:
            break
            
    phonebook_db.insert(target_pos, new_entry)
    print("New element has been added")
    return

def deleteElement():
    name_to_remove = input("Please enter name to be deleted: ")
    remove_index = -1
    
    for entry in phonebook_db:
        if name_to_remove == entry["student_name"]:
            remove_index = phonebook_db.index(entry)
            break
            
    if remove_index == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(remove_index))
        del phonebook_db[remove_index]
    return

def editStudent():
    name_to_edit = input("Please enter name to be updated: ")
    
    edit_index = -1
    for entry in phonebook_db:
        if name_to_edit == entry["student_name"]:
            edit_index = phonebook_db.index(entry)
            break
            
    if edit_index == -1:
        print("Element was not found")
    else:
        del phonebook_db[edit_index]
        
        print("Enter new info:")
        updated_name = input("Please enter student name: ")
        updated_phone = input("Please enter student phone: ")
        updated_email = input("Please enter student email: ")
        updated_group = input("Please enter student group: ")
        
        edited_entry = {"student_name": updated_name, "mobile": updated_phone, "email_addr": updated_email, "study_group": updated_group}
        
        insert_idx = 0
        for entry in phonebook_db:
            if updated_name > entry["student_name"]:
                insert_idx += 1
            else:
                break
                
        phonebook_db.insert(insert_idx, edited_entry)
        print("Data updated. Sorting applied.")
    return

def main():
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
                break
            case _:
                print("Wrong chouse")

main()