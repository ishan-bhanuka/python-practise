class PropAccount:

    def __init__(self, firm_name, initial_balance):
        self.name = firm_name
        self.balance = initial_balance
        self.min_allowed_balance = initial_balance * 0.90
        self.is_active = True

        # අලුතින් එකතු කරන State Variables (Attributes)
        self.total_trades = 0
        self.winning_trades = 0

    def trade_closed(self, profit_loss):
        if not self.is_active:
            print(f"[{self.name}] ❌ Account is BLOWN!")
            return

        # Trades ගණන අප්ඩේට් කිරීම
        self.total_trades += 1
        if profit_loss > 0:
            self.winning_trades += 1

        self.balance += profit_loss
        print(
            f"[{self.name}] Trade #{self.total_trades} | P/L: ${profit_loss} |"
            f" Balance: ${self.balance}"
        )

        if self.balance < self.min_allowed_balance:
            self.is_active = False
            print(f"🚨 [{self.name}] Account BLOWN!")

    # Win Rate එක Calculate කරලා දෙන Method එකක්
    def get_win_rate(self):
        if self.total_trades == 0:
            return 0.0

        win_rate = (self.winning_trades / self.total_trades) * 100
        return win_rate


# Test කරමු
my_acc = PropAccount("FTMO", 100000)
my_acc.trade_closed(1500)  # Trade 1: Win
