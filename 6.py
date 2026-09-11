raw_data =[1, 3, 5, 3, 7, 1, 9, 5, 2]
clean_data = []

for i in raw_data:
    if i not in clean_data:
        clean_data.append(i)
    else:
        continue
print(clean_data)