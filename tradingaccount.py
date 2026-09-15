class trading_account:
    account_count=0
    def __init__(self,account_ID,balance):
        self.account_ID=account_ID
        self.__balance=balance
        self.trading_history=[]
        self.trade_count=0
        self.lost_trades=0
        trading_account.account_count+=1
    @property
    def balance(self):
        return f'Your account balance:{self.__balance}'
#    @balance.setter                             You told me to add this , but I don't think it's a good idea, why do we let them change the balance?
#    def balance(self,new_balance):
#        if new_balance<0:                
#            print('ERROR!!')
#            return
#        self.__balance=new_balance
    def trade(self,PnL):
        if self.__balance<=10:
            print('You should have at least 10$ dollars to trade')
            return
        self.trade_count+=1
        if PnL<0:
            self.__balance+=PnL
            if self.__balance<=10:
                print('You should have at least 10$ dollars to trade')
                self.__balance=0
                return
            self.trading_history.append(f'trade {self.trade_count} PnL:{PnL}')
            self.lost_trades+=1
        else:
            self.__balance+=PnL
            self.trading_history.append(f'trade {self.trade_count} PnL:{PnL}')
    def __str__(self):
        return(f"Account ID:{self.account_ID} | Account balance:{self.__balance}")
    @property
    def history(self):
        return self.trading_history
account1=trading_account(2342342423,1000)
account2=trading_account(4745324325,2000)
account3=trading_account(5334276833,1500)
account1.trade(-233)
account1.trade(356)
account1.trade(-3544)

print(account1.balance)
print(account1.history)
print(account1)