# region imports
from AlgorithmImports import *
# endregion

class VirtualLightBrownManatee(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetEndDate(2021,1,1)
        self.SetCash(10000000)  # Set Strategy Cash
        # self.AddEquity("SPY", Resolution.Daily)

        ## set up our universe
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelection,self.FineSelection)

    def CoarseSelection(self,coarse):
        ## coarse == giant list of 8000 equities

        self.filtered_by_price = [x.Symbol for x in coarse if x.Price > 20 \
            and x.DollarVolume > 10000000 and x.HasFundamentalData]

        return self.filtered_by_price

    def FineSelection(self,fine):
        self.filtered_by_pe = [sec for sec in fine if sec.ValuationRatios.PERatio < 100]

        sorted_by_ebit = sorted(self.filtered_by_pe,key=lambda x:x.FinancialStatements.IncomeStatement.EBIT.TwelveMonths,reverse=True)

        list_of_symbols = [x.Symbol for x in sorted_by_ebit]

        return list_of_symbols

    def OnData(self, data: Slice):

        self.Log(self.Time)

        for sec in self.Securities.Values:

            if not data.ContainsKey(sec.Symbol) or not data[sec.Symbol]:
                return

            self.Log(f"{data[sec.Symbol].Symbol} opened at {data[sec.Symbol].Open}")

        self.Log("---------------------")


    def OnSecuritiesChanged(self, changes):
        self.Log("CHANGE IN UNIVERSE")

        for sec in changes.RemovedSecurities:
            self.Liquidate(sec.Symbol)
            self.Log(f"Sold: {sec}")

        for sec in changes.AddedSecurities:
            self.SetHoldings(sec.Symbol,0.1)
            self.Log(f"BOUGHT: {sec}")
