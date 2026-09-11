try:
   class riskmanager:
       max_leverage=100
       def __init__(self,leverage):
           if leverage>riskmanager.max_leverage:
               print(f'Max leverage is {riskmanager.max_leverage}!')
               return
           self.__leverage=leverage
       @property
       def leverage(self):
           return self.__leverage
       @leverage.setter
       def leverage(self,new_leverage):
           if riskmanager.max_leverage<new_leverage:
               print(f'Max leverage is {riskmanager.max_leverage}!')
               return
           self.__leverage=new_leverage
   account1=riskmanager(40)

except AttributeError:
    print(f"You haven't set your leverage yet!!  Max leverage is {riskmanager.max_leverage}! ")
account1.leverage=333
account1.leverage=100
print(account1.leverage)