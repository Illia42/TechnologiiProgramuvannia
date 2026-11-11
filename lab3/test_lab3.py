from Student import Student
from StudentList import StudentList

def test_insert_record():
    
    sl = StudentList()
    student = Student("Denis", "0934445560", "denis@mail.com", "KB-252")
    
  
    sl.insert(student)
    

    assert len(sl.students) == 1
    assert sl.students[0].name == "Denis"
    assert sl.students[0].group == "KB-252"

def test_remove_record():
    
    sl = StudentList()
    student = Student("Ivan", "0667654321", "ivan@mail.com", "KB-252")
    sl.insert(student)
    assert len(sl.students) == 1
    
    
    result = sl.remove("Ivan")
    
    
    assert result == True
    assert len(sl.students) == 0