class Account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
        
class Saving_Account(Account):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate = interest_rate

class Risk_Limits:
    def __init__(self,max_loss):
        self.max_loss = max_loss

class Prop_Account(Account , Risk_Limits):
    def __init__(self,account_number,balance,max_loss):
            Account.__init__(self,account_number,balance)
            Risk_Limits.__init__(self,max_loss)

