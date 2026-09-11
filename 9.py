student_marks = [75, 42, 88, 65, 30, 95, 50]
total=0
As=[]
for x in student_marks:
    total=total+x
    if x>=75:
        As.append(x)
print(f'TOtal={total}')
print(f'Average={total/(len(student_marks))}')
print(f'No. of A grades={len(As)}')