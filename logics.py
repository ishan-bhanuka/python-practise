a=float(input('Length of the first side of the triangle  -'))
b=float(input('Length of the second side of the triangle  -'))
c=float(input('Length of the third side of the triangle  -'))
if(a >b):
    if(a>c):
        one=a
        two=b
        three=c
    else:
        one=c
        two=b
        three=a
elif(b>c):
    one=b
    two=a
    three=c
else:
    one=c
    two=b
    three=a

if(one<two+three):
    print('This is a valid triangle.')
    if(one==two==three):
        print('Equilateral triangle')
    elif(one==two):
        print('Isosceles triangle')
    elif(one==three):
         print('Isosceles triangle')
    elif(two==three):
         print('Isosceles triangle')
    else:
        print('Scalene triangle')
else:
    print('This is not a valid triangle')