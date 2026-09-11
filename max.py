def analyze_marks(marks_list):
    x=max(marks_list)
    y=min(marks_list)
    for x in marks_list:
        total=0
        total=total+x
    avg=total/len(marks_list)
    return max,min,avg
marks_list=[70, 85, 40, 90, 65]
max,min,avg=(analyze_marks(marks_list))
print(f'Max={max}')
print(f'Min={min}')
print(f'Average={avg}')