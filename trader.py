class trader:
    def __init__(self,name,strategy):
        self.name=name
        self.strategy=strategy
    def __str__(self):
        return(f"Name:{self.name},Strategy:{self.strategy}")
trader1=trader('Ishan','Support and Resistance')
print(trader1)
# or print(trader1.__dict__)