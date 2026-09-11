def evaluate_student(student_dict):
    if student_dict["marks"]>100:
        print("Invalid")
        return "Error","Error"
    elif student_dict["marks"]>=75:
        return "A","pass"
    elif student_dict["marks"]>=50:
        return "B","Pass"
    else:
        return "F","Fail"
student1 = {"name": "Ishan", "marks": 80}
grade,status=evaluate_student(student1)
print(f"Grade:{grade} and Status:{status}")