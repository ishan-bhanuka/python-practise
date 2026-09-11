def error_handling():
    k=0
    while k==0:
     try:    
       num1=int(input("Enter the first number-"))
       num2=int(input("Enter the second number-"))
       print(num1/num2)
       break
     except ZeroDivisionError:
        print("Can't devide by zero!")
        break
     except ValueError:
        print("ONLY enter a number!")
error_handling()