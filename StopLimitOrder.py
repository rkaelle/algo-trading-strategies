# region imports
from AlgorithmImports import *
# endregion

class CreativeFluorescentPinkChinchilla(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetStartDate(2021, 1, 1)
        self.SetCash(100000)  # Set Strategy Cash
        self.spy = self.AddEquity("SPY", Resolution.Daily)

    def OnData(self, data):

        if not self.Portfolio.Invested:
            close = self.Securities['SPY'].Close
            ## 1% drop a stop is trigered
            stop_price = close * 0.99
            # limit of 1% above the close price
            limit_price = close * 1.01

            self.StopLimitOrder(self.spy.Symbol, 10, stop_price, limit_price)