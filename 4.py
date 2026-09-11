numbers=[]
while True:
    num=int(input("Enter a number->"))
    if num<0:
        break
    else:
        numbers.append(num)
print(f"The length of your list is {len(numbers)}.")
