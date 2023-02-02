#region imports
from AlgorithmImports import *
#endregion
class SmoothOrangeHyena(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2008, 1, 1)  # Set Start Date
        self.SetCash(10000)  # Set Strategy Cash
        self.ibm = self.AddEquity("IBM",Resolution.Daily)

        self.Invest=True


    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.Invest:
            ## buy 10 shares, max price 50$
            self.LimitOrder(self.ibm.Symbol,10,50)
            self.LimitOrder(self.ibm.Symbol,-10,100)
            self.Invest=False