import random
secret_number=random.randint(1,50)
def number_gusseng():
   k=0
   while k==0:
     try:
       while True:
          your_turn=int(input("Enter a number between 1-50->"))
          k=1
          if 1<your_turn<50:
            if secret_number<your_turn:
                print("වැඩියි මචං, තව අඩු කරපන්!")
            elif secret_number>your_turn:
                print("මදි මචං, තව වැඩි කරපන්!")
            else:
                print("සුපිරි! උඹ දින්නා!")
                break
          else:
             print("Enter a number between the given range!!!!")
     except ValueError:
        print("කරුණාකර ඉලක්කමක් පමණක් ඇතුළත් කරන්න!")

number_gusseng()