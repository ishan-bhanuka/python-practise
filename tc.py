# 1. ප්ලෑන් එක හදමු (Class එක)
class TradingAccount:
    
    # මේක තමයි Account එකක් හැදෙනකොටම මුලින්ම Run වෙන Setup Function එක.
    # self කියන්නේ 'මේ අදාළ අකවුන්ට් එක' කියන එකයි.
    def __init__(self, account_name, initial_balance):
        self.name = account_name
        self.balance = initial_balance

    # මේක Account එකෙන් කරන්න පුළුවන් වැඩක් (Method)
    def show_balance(self):
        print(f"{self.name} Account Balance: ${self.balance}")


# 2. අර ප්ලෑන් එක (Class) පාවිච්චි කරලා සැබෑ අකවුන්ට් (Objects) දෙකක් හදමු!
demo_account = TradingAccount("My Demo", 10000)
prop_account = TradingAccount("FundingPips", 50000)

# 3. දැන් ඒ Objects වල තියෙන වැඩ (Functions) කරවලා බලමු
demo_account.show_balance()
prop_account.show_balance()