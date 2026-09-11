import time
print("Nasa is hacking!")
for x in range(1,101):
    print(f"\r{x}%",end='')
    time.sleep(x/20)