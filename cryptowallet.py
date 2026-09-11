try:
   class crytowallet:
       def __init__(self,privatekey,balance):
           self.__privatekey=privatekey
           self.balance=balance

   wallet1=crytowallet('fuiy7834876vh3784rfcbY&^*&6',1000)
   wallet2=crytowallet('fsufy8736UF&^UIY$%*_',2000)
   print(wallet1.__privatekey)

except AttributeError:
    print("You don't have permission to access Privatekey!!")
print(wallet1.__dict__)
print(wallet2.__dict__)