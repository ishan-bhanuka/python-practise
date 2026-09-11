class symbol:
    def __init__(self,ticker,timeframe='1H'):
        self.ticker=ticker
        self.timeframe=timeframe
    def __str__(self):
        return(f"Ticker:{self.ticker}, Timeframe:{self.timeframe}")
symbol1=symbol(27)
print(symbol1)
symbol2=symbol(38,'3min')
print(symbol2)
