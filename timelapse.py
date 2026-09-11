import time
print("Your PC is being hacked!")
for x in range(1,101):
    print(f"\r{x}%",end='')
    time.sleep(x/100)
while True:
    print("Hacked,you are COOKED!!")