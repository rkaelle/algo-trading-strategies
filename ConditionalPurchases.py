# region imports
from AlgorithmImports import *
# endregion

class DancingMagentaDonkey(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 1, 1)  # Set Start Date
        self.SetEndDate(2020, 3, 1)
        self.SetCash(100000)  # Set Strategy Cash
        self.vnq = self.AddEquity("VNQ", Resolution.Minute)
        self.vnqi = self.AddEquity("VNQI", Resolution.Minute)


    def OnData(self, data: Slice):
        vnqi_gain = (self.vnqi.Close - self.vnqi.Open)/self.vnqi.Open 
        vnq_gain = (self.vnq.Close - self.vnq.Open)/self.vnq.Open


        ##if not self.Portfolio.Invested:
            ##self.SetHoldings("SPY", 0.33)

        ## Daily Gain (2%)

        # VNQI gain > 2% and VNQI gain > VNQ gain 
        # 100% holdings into VNQ
        if vnqi_gain > 0.02 and vnqi_gain > vnq_gain:
            self.SetHoldings(self.vnq.Symbol,1,True)
            self.Log(f"VNQI Gain: {vnqi_gain}")

        #vnq > 2% and VNQ gain > VNQI gain
        ## 100% holdings vnqi
        if vnq_gain > 0.02 and vnq_gain > vnqi_gain:
            self.SetHoldings(self.vnqi.Symbol,1,True)
            self.Log(f"VNQ Gain: {vnq_gain}")

        else: 
            self.Log("no action taken")