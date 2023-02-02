# region imports
from AlgorithmImports import *
# endregion

class FormalFluorescentOrangeBison(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 1, 1)  # Set Start Date
        self.SetCash(10000)  # Set Strategy Cash
        self.spy = self.AddEquity("SPY", Resolution.Daily)
        self.Securities['SPY'].SetLeverage(100)
        self.invest = True

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("SPY", 99)
            self.invest = False

    def OnMarginCall(self,requests):

        ## Margin Call --> 10% more

        for order in requests:
            new_quantity = int(order.Quantity*1.1)
            requests.remove(order)
            new_order = SubmitOrderRequest(order.OrderType,order.SecurityType,order.Symbol,new_quantity,order.StopPrice,order.LimitPrice,self.Time,'OnMarginCall')
            requests.append(new_order)
        return requests
    ###def OnMarginCallWarning(self):
        ###self.log(f"Margin: {self.Portfolio.MarginRemaining}")
        ###self.Liquidate(self.spy.Symbol)