class trading_account:
    total_accounts=0
    def __init__(self,account_name,initial_balance):
        self.name=account_name
        self.__balance=initial_balance
        trading_account.total_accounts+=1

    def trade_closed(self,profit_loss):
        self.__balance+=profit_loss
    def show_balance(self):
        print(f"Balance:{self.__balance}")
    def __str__(self):
        return (f"Account: {self.name} | Balance: ${self.__balance}")

my_acc=trading_account("FTMO",100000)
your_acc=trading_account("fundingpips",14555555)
print(trading_account.total_accounts)

print(my_acc.__str__())