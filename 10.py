balance=1000
history=[]
while True:
   print('''--- MORA BANK SYSTEM ---
   1. Deposit Money (මුදල් තැන්පත් කිරීම)
   2. Withdraw Money (මුදල් ලබාගැනීම)
   3. Check Balance (ශේෂය පරීක්ෂාව)
   4. Transaction History (ගනුදෙනු වාර්තාව)
   5. Exit (පිටවීම)''')
   option=int(input(print('Select an option-')))
   if option==1:
      deposit=int(input(print('Enter the amount you want to deposit-')))
      balance=balance+deposit
      history.append(f'Deposited: Rs.{deposit}')
   elif option==2:
      withdraw=int(input(print('Enter the amount you want to withdraw-')))
      if withdraw<balance:
         balance=balance-withdraw
         history.append(f'Withdrew: Rs.{withdraw}')
      else:
         print("Insufficient Balance")
   elif option==3:
      print(f'Blance:Rs.{balance}')
   elif option==4:
      for x in range(1,len(history)+1):
         print(f'({x}).{history[x-1]}')
   elif option==5:
      print('Thank you!')
      break
