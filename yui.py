class PropAccount:
    
    # 1. අකවුන්ට් එකක් හැදෙනකොටම නමයි බැලන්ස් එකයි සෙට් කරනවා
    def __init__(self, firm_name, initial_balance):
        self.name = firm_name
        self.balance = initial_balance
        
    # 2. ට්‍රේඩ් එකක් ක්ලෝස් වුණාම බැලන්ස් එක අප්ඩේට් කරන Method එක
    def trade_closed(self, profit_loss):
        self.balance = self.balance + profit_loss
        print(f"[{self.name}] Trade Closed! New Balance: ${self.balance}")

# ---------------------------------------------------------
# අච්චුවෙන් සැබෑ Accounts (Objects) දෙකක් හදමු
# ---------------------------------------------------------
ftmo_acc = PropAccount("FTMO", 100000)
pips_acc = PropAccount("FundingPips", 5000)

# දැන් ට්‍රේඩ් කරලා බලමු!
ftmo_acc.trade_closed(500)    # FTMO එකේ $500 ක ප්‍රොෆිට් එකක් (US30 Trade)
pips_acc.trade_closed(-200)   # FundingPips එකේ $200 ක ලොස් එකක් (XAUUSD Trade)
PropAccount.trade_closed(ftmo_acc,500)
PropAccount.trade_closed(pips_acc,-200)