from lab2 import insert_record, remove_record, phonebook_db

def test_insert_record():

    phonebook_db.clear()

    
    insert_record("Denis", "0934445560", "denis@mail.com", "KB-252")

    
    assert len(phonebook_db) == 1
    assert phonebook_db[0]["student_name"] == "Denis"
    assert phonebook_db[0]["study_group"] == "KB-252"

def test_remove_record():
    phonebook_db.clear()

    
    insert_record("Ivan", "0667654321", "ivan@mail.com", "KB-252")
    assert len(phonebook_db) == 1

    
    result = remove_record("Ivan")
    assert result == True

    
    assert len(phonebook_db) == 0