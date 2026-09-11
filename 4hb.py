marks = [55, 32, 85, 42, 90, 73, 28]
paas=[]
fail=[]
for i in marks:
    if i<50:
        fail.append(i)
        print(f'{i} is fail.')
    else:
        paas.append(i)
        print(f'{i} is pass.')
print('Total pass:',len(paas))
print('Total fail:',len(fail))

