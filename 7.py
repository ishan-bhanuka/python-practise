correct_password = "MoraEng2026"
attempt=0
k=0
password=input('Enter the password-')
while attempt<2:
    attempt=attempt+1
    if len(password)<len(correct_password):
      print("Password එක දිග මදි!")
      password=input('Enter the password-')
      continue
      
    elif password==correct_password:
       k=2
       break
    else:
       print('Your password is wronng!')
       password=input('Enter the password-')
  
if k==2:
   print("Access Granted! 🔓")
else:
   print("System Locked! ❌")