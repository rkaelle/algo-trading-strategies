# region imports
from AlgorithmImports import *
# endregion

class SmoothOrangeHyena(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2010, 1, 1)  # Set Start Date
        self.SetEndDate(2015,1,1)
        self.SetCash(100000)  # Set Strategy Cash
        self.stock = self.AddEquity("SPY",Resolution.Daily)

        self.Invest=True


    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.Invest:
            self.MarketOrder(self.stock.Symbol,1000)
            self.Invest=False

        if self.Time == datetime(day=1,month=1,year=2014):
            self.MarketOrder(self.stock.Symbol, -1000)