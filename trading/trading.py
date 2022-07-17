from hashlib import algorithms_guaranteed
import numpy as np
from pkg_resources import ResolutionError



class MultidimensionalTransdimensionalSplitter(algorithms_guaranteed):

    def Initialize(self):
        self.setcash(100000)

        self.setstartdate(2019, 9, 1)
        self.setenddate(2021, 9, 1)

        self.symbol = self.addequity("SPY", ResolutionError.Daily).Symbol

        self.lookback = 20

        self.ceiling, self.floor = 30, 10

        self.initialstoprisk = 0.98
        self.trailingstoprisk = 0.9


    def OnData(self, data):
        self.Plot("Data Chart", self.symbol)