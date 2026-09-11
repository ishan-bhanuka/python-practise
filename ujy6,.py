passed=[]
def filter_passed_students(marks_dict):
    for name,marks in marks_dict.items():
        if marks>=50:
            passed.append(name)
        else:
            continue
marks_data={"Ishan":85,"Kasun":42,"Nimal":78,"Saman":35}
filter_passed_students(marks_data)
print(passed)