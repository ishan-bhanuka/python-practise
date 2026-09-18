class Trader:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def show_info(self):
        print(f'Account name:{self.name} | Account balance:{self.balance}')

class Forex_Trader(Trader):
    def __init__(self,name,balance,prop_firm):
        super(). __init__(name,balance)
        self.prop_firm=prop_firm

    def trade(self,pair):
        print(f'{self.name} is trading {pair}.')

class Crypto_Trader(Trader):
    def __init__(self,name,balance,trading_platform):
        super().__init__(name,balance)
        self.trading_platform=trading_platform



trader1=Forex_Trader('Ishan',1000,'FTMO')
trader2=Crypto_Trader('Bhanuka',2000,'Binance')
print(trader1.name)
print(trader1.balance)
print(isinstance(trader1,Forex_Trader))
print(issubclass(Forex_Trader,Trader))
print(trader1.prop_firm)
trader1.trade('AUDUSD')
trader1.show_info()