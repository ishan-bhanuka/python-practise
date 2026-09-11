guests = ["Ishan", "Kasun", "Nimal", "Kamal", "Ruwan", "Nimali"]
name=input("Enter a guest's name-")
k=1
for i in guests:
    if name==i:
        k=2
        break
if k==2:
    guests.remove(i)
    print(guests)
else:
    print("Your guest's name is not in the list")
