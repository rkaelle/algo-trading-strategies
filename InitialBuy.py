class BuyAndHold(QCAlgorithm):

    def Initialize(self):

        self.SetStartDate(2015,1,1)

        self.SetEndDate(2020,1,1)

        self.SetCash(10000)

        self.AddEquity('AAPL',Resolution.Daily)

    def OnData(self,data):
	    if not self.Portfolio.Invested:
		    self.SetHoldings('AAPL',1)
