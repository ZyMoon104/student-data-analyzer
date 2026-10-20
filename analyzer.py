import csv

def load_student(filename):
    try:
        with open(filename,"r",encoding="utf-8") as f:
            reader = csv.DictReader(f)
            students=[]
            for row in reader:
                students.append(row)
            return True,students
    except FileNotFoundError:
        return False,"找不到文件"

def calculate_score(students):
    students_score=[]
    if not students:
        return None
    else:
        for student in students:
            students_score.append(float(student["score"]))
        average_score=sum(students_score)/len(students_score)
        return average_score

def find_top_student(students):
    max_score=max(students,key=lambda x:float(x["score"]))
    return max_score

def count_students(students):
    pass_count=0
    for student in students:
        if float(student["score"])>=60:
            pass_count+=1
    return pass_count

def validate_student(student):
    try :
        student["name"]
        if not student["name"]:
            return False,"姓名不存在或为空"
    except KeyError:
        return False,"姓名不存在或为空"
    try:
        student["age"]
        try:
            int(student["age"])
        except ValueError:
            return False,"年龄不为整数"
    except KeyError:
        return False,"年龄不存在或为空"
    try:
        student["score"]
        try:
            score=float(student["score"])
        except ValueError:
            return False,"成绩不是数字"
        else:
            if score < 0 or score > 100:
                return False,"成绩超出范围"
    except KeyError:
        return False,"成绩不存在或为空"
    return True,"核验通过"

def clean_students(students):
    valid_students=[]
    invalid_students=[]
    for student in students:
        result=validate_student(student)
        if result[0]:
            valid_students.append(student)
        if not result[0]:
            invalid_students.append((student,result[1]))
    return valid_students,invalid_students

def process_students_file(filename):
    get_students = load_student(filename)
    if not get_students[0]:
        return False,None,"找不到文件"
    else:
        students=get_students[1]
        valid_students, invalid_students = clean_students(students)
        return True,valid_students,invalid_students

if __name__ == "__main__":
    result = process_students_file("data/students.csv")
    print(result)