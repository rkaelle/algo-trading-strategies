# region imports
from AlgorithmImports import *
# endregion

class SwimmingBlueKangaroo(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 1, 1)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.AddEquity("SPY", Resolution.Daily)

        price_plot = Chart("Custom Chart")
        price_plot.AddSeries(Series('Price',SeriesType.Line,0))
        self.AddChart(price_plot)

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)

        self.Plot("Custom Chart","Price",self.Securities['SPY'].Open)
        