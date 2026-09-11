class propfirmaccount:
    def __init__(self,max_drawdown):
        self.__max_drawdown=max_drawdown
    @property
    def max_drawdown(self):
        return f'{self.__max_drawdown}%'
    @max_drawdown.setter
    def max_drawdown(self,new_max_drawdown):
        if new_max_drawdown>10:
            print('ERROR! Max drawdown is 10%')
            return
        self.__max_drawdown=new_max_drawdown

account1=propfirmaccount(5)
print(account1.max_drawdown)
account1.max_drawdown=4
print(account1.max_drawdown)
account1.max_drawdown=45
print(account1.max_drawdown)
