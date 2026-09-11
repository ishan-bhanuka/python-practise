numbers=[12, 7, 22, 19, 5, 8, 31, 40]
even_numbers=[]
odd_numbers=[]
for i in numbers:
    x=i%2
    if x==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(f'even numbers={even_numbers}')
print(f'odd numbers={odd_numbers}')

