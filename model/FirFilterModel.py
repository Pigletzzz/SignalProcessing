from scipy import signal

from model.FilterModel import FilterModel, FilterType, PassbandType, WindowType


# FIR滤波器Model类
class FirFilterModel(FilterModel):
    def __init__(self, sampleRate: int, cutoffFreq, passband: PassbandType, order: int, window: WindowType):
        super().__init__(FilterType.FIR, sampleRate, cutoffFreq, passband)

        self.b = signal.firwin(order + 1, cutoffFreq / sampleRate, window=window.value, pass_zero=passband.value)
        self.a = 1
        print("b = " + str(self.b))
        print("a = " + str(self.a))
