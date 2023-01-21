class SellAfterTime(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 1, 1)  # Set Start Date
        self.SetEndDate(2021,1,1)
        self.SetCash(10000)  # Set Strategy Cash
        self.AddEquity("SPY",Resolution.Daily)
        self.invest = True

    def OnData(self, data: Slice):

        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("SPY", 1)
            self.invested_time = self.Time ## DATETIME
        
        ## Liquidatre after 1000 days
        self.Log(self.Time-self.invested_time)
        time_diff = (self.Time - self.invested_time).days
        if time_diff > 1000:
            self.Liquidate("SPY")
            self.invest = False
