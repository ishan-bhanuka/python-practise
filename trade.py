class trade:
    def __init__(self,pair,lotsize,type):
        self.pair=pair
        self.lotsize=lotsize
        self.type=type
    def __str__(self):
        return(f"[{self.type}] {self.pair} - {self.lotsize} Lots")
trade1=trade('EURUSD',1.00,'BUY')
print(trade1)