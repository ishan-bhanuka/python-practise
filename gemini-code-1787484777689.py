class PropAccount:
    
    def __init__(self, firm_name, initial_balance):
        self.name = firm_name
        self.balance = initial_balance
        
        # 1. 10% ක Max Loss සීමාව ගණනය කරලා තියාගමු (දත්තයක් විදිහට)
        self.min_allowed_balance = initial_balance * 0.90 
        
        # 2. අකවුන්ට් එක තාම හොඳ තත්ත්වයේ තියෙනවද කියලා බලන Variable එක
        self.is_active = True 
        
    def trade_closed(self, profit_loss):
        
        # ට්‍රේඩ් එකක් දාන්න කලින් අකවුන්ට් එක ඇක්ටිව් ද කියලා බලනවා
        if self.is_active == False:
            print(f"[{self.name}] ❌ You can't trade! Account is BLOWN!")
            return  # අකවුන්ට් එක බ්ලෝන් නම් මෙතනින්ම function එකෙන් එළියට යනවා
            
        # ට්‍රේඩ් එක අකවුන්ට් එකට දානවා
        self.balance = self.balance + profit_loss
        print(f"[{self.name}] Trade Closed! P/L: ${profit_loss} | New Balance: ${self.balance}")
        
        # 3. Drawdown ලිමිට් එක පැනලාද කියලා චෙක් කිරීම
        if self.balance < self.min_allowed_balance:
            self.is_active = False # ලිමිට් පැනලා නම් අකවුන්ට් එක අක්‍රිය කරනවා
            print(f"🚨 🚨 ALERT: [{self.name}] Account BLOWN! Max drawdown reached! 🚨 🚨")

# ---------------------------------------------------------
# අච්චුවෙන් සැබෑ Account එකක් හදමු
# ---------------------------------------------------------
my_ftmo = PropAccount("FTMO", 100000)

# දැන් ට්‍රේඩ් කරලා බලමු!
my_ftmo.trade_closed(5000)    # $5,000 Profit
my_ftmo.trade_closed(-10000)  # $10,000 Loss (දැන් බැලන්ස් 95,000 යි)
my_ftmo.trade_closed(-6000)   # $6,000 Loss (දැන් බැලන්ස් 89,000 යි - 90,000 ලිමිට් එක පනිනවා!)
my_ftmo.trade_closed(2000)    # මේක දාන්න ගියාම මොකද වෙන්නේ බලපන්...