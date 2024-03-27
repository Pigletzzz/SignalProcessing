from scipy import signal

from entity.Filter import FilterType, PassbandType, WindowType


# 滤波器Model基类
class FilterModel(object):
    # def __init__(self, filterType: FilterType, sampleRate: int, cutoffFreq,
    #              passband: PassbandType):
    #     self.sampleRate = sampleRate
    #     self.filterType = filterType
    #     self.passband = passband
    #
    #     self.b = 1
    #     self.a = 1

    def __init__(self):
        self.h = None
        self.w = None
        self.passband = None
        self.sampleRate = None
        self.b = None
        self.a = None
        self.filter = None
        self.nfft = 4096

    def firDesign(self, sampleRate: int, cutoffFreq1, cutoffFreq2, passband: PassbandType, order: int,
                  window: WindowType):
        if passband == PassbandType.LOWPASS or passband == PassbandType.HIGHPASS:
            cutoffFreq = cutoffFreq1 / sampleRate
        else:
            cutoffFreq = [cutoffFreq1 / sampleRate, cutoffFreq2 / sampleRate]
        self.b = signal.firwin(order + 1, cutoffFreq, window=window.value, pass_zero=passband.value)
        self.a = 1

        self.filter = FilterType.FIR
        self.passband = passband
        self.sampleRate = sampleRate
        # self.filter = Filter(FilterType.FIR, sampleRate, passband, b, 1)

        # 求出频率响应
        self.w, self.h = signal.freqz(self.b, self.a, worN=self.nfft)

    # 获取频率响应
    def getFreqz(self):
        return self.w, self.h, self.sampleRate, self.nfft
