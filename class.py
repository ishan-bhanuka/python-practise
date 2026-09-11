class account:
    def __init__(self,account_number):
        self.__account_number=account_number
    @property
    def account_number(self):
        return self.__account_number
account1=account(35434353535)
print(account1.account_number)