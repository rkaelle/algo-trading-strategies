class SellOnProfit(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2010, 1, 1)  # Set Start Date
        self.SetEndDate(2021,1,1)
        self.SetCash(10000)  # Set Strategy Cash
        self.AddEquity("AAPL", Resolution.Daily)

        self.invest = True

        ## 100% profit --> Sell
        self.limit_profit_percent = 1

    def OnData(self, data: Slice):

        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("AAPL", 1)

        profit_percent = self.Portfolio['AAPL'].UnrealizedProfitPercent

        if profit_percent > self.limit_profit_percent:
            self.Liquidate("AAPL")
            self.invest=False