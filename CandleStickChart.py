# region imports
from AlgorithmImports import *
# endregion

class HipsterGreenCrocodile(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2017, 1, 1)  # Set Start Date
        self.SetEndDate(2020,1,1)
        self.SetCash(100000)  # Set Strategy Cash
        self.AddEquity("SPY", Resolution.Daily)

        price_plot = Chart("Candle Plot")
        price_plot.AddSeries(Series("Price",SeriesType.Candle,0))
        self.AddChart(price_plot)

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)

        self.Plot("Candle Plot","Price",self.Securities["Spy"].Price)