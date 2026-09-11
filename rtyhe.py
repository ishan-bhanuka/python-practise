def check_student_pass(student_dict):
    if student1["marks"]>=50:
        return("Pass")
    else:
        return("Fail")
student1={"name":"Ishan","marks":75}
x=check_student_pass(student1)
print(x)