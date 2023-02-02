# region imports
from AlgorithmImports import *
# endregion

class SquareMagentaChinchilla(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetCash(10000)  # Set Strategy Cash
        self.seaworld = self.AddEquity("SEAS", Resolution.Daily)
        self.invest=True

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.invest:
            ## Short = Sell without owning/Purchasing First
            self.SetHoldings(self.seaworld.Symbol, -1)

        if self.Time.month == 5:
            self.Liquidate(self.seaworld.Symbol)
            self.invest=false