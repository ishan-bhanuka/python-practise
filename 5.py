data = [45, 12, 89, 33, 7, 67]
max=float('-inf')
min=float('inf')
for i in range(len(data)):
    if max<data[i]:
        max=data[i]
    elif min>data[i]:
        min=data[i]
print(f'Max is {max} and min is {min}')
