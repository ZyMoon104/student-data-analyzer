from analyzer import count_students
from analyzer import validate_student
from analyzer import clean_students
from analyzer import load_student
def test_count_students():
    students1 = [
        {"name": "A", "score": "59"},
        {"name": "B", "score": "60"},
        {"name": "C", "score": "100"}
    ]
    result1=count_students(students1)
    assert result1 == 2

def test_clean_student():
    students2 = [
        {"name": "Alice", "age": "20", "score": "85"},
        {"name": "Bob", "age": "abc", "score": "80"},
        {"name": "Cindy", "age": "21", "score": "95"}
    ]
    result2=clean_students(students2)
    assert len(result2[0]) == 2
    assert len(result2[1]) == 1

def test_validate_student():
    students3 = [
        {"name": "Alice", "age": "20", "score": "85"},
        {"name": "", "age": "20", "score": "85"},
        {"name": "Bob", "age": "abc", "score": "85"},
        {"name": "Bob", "age": "20", "score": "hello"},
        {"name": "Bob", "age": "20", "score": "101"}
    ]
    result3=validate_student(students3[0])
    assert result3[0] == True
    result3=validate_student(students3[1])
    assert not result3[0]
    result3=validate_student(students3[2])
    assert not result3[0]
    result3=validate_student(students3[3])
    assert not result3[0]
    result3=validate_student(students3[4])
    assert not result3[0]

def test_load_student_success():
    students4 = load_student("data/students.csv")
    assert students4[0] == True


def test_load_student_not_found():
    students5 = load_student("data/students_not_found.csv")
    assert not students5[0]