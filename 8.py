prime=int(input('Enter a number-'))
x=[]
for i in range(1,prime+1):
    if prime%i==0:
        x.append(i)
if len(x)==2:
    print(f'{prime} is a prime number.')
else:
     print(f'{prime} is not a prime number.')