import sys
import time
import numpy as np
import os

from dcps import AimTTiPLP
import setupStatus

class Magfield:
    def __init__(self, setupNr, resource, channel):
        self.setup = setupStatus.setup_status[str(setupNr)]
        self.setupNr = setupNr
        self.number_coils = len(self.coil_list)
        self.coversion_params = self.setup["conversionGauss2Amp"]
        self.current_limits = self.setup["limitCurrent"]
        self.max_volt = self.setup["maxVolt"]
        self.rate_limits = setl.setup["limitRate"]
        self.ramping = False
        self.stop_ramp = False
        self.ps = []
        self.volt_meas = []
        self.curr_meas = []
        self.curr_set =  []
        self.volt_set = []
        self.channel = channel

    # Generate power supply
        self.resource = environ.get('aimtti', resource)
        self.ps = AimTTiPLP(self.resource)
        self.ps.open()

    # Get status
        volt = float(self.ps.measureVoltage(channel=self.channel))
        self.volt_meas.append(volt)
        curr = float(self.ps.measureCurrent(channel=self.channel))
        self.curr_meas.append(curr)

        volt_set = float(self.ps.queryVoltage(channel=self.channel))
        self.volt_set.append(volt_set)
        curr_set = float(self.ps.queryCurrent(channel=self.channel))
        self.curr_set.append(curr_set)



    def get_status(self,channel=None):
