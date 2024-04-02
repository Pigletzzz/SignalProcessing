from scipy import signal

from entity.Filter import FilterType, PassbandType, WindowType, ProtoType


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

    def iirDesign(self, sampleRate: int, passbandLow: int, passbandHigh: int, stopbandLow: int, stopbandHigh: int,
                  Rp: float, As: float, passband: PassbandType, protoTypes: ProtoType):
        # 计算参数
        fn = sampleRate / 2
        if (passband == PassbandType.LOWPASS or passband == PassbandType.HIGHPASS):
            wp = passbandLow / fn
            ws = stopbandLow / fn
        else:
            wp = [passbandLow / fn, passbandHigh / fn]
            ws = [stopbandLow / fn, stopbandHigh / fn]

        # 分别计算滤波器参数
        if protoTypes == ProtoType.BUTTERWORTH:
            N, Wn = signal.buttord(wp, ws, Rp, As, analog=True)
            b, a = signal.butter(N, Wn, btype=passband.value, analog=True)
        elif protoTypes == ProtoType.CHEBYSHEV1:
            N, Wn = signal.cheb1ord(wp, ws, Rp, As, analog=True)
            b, a = signal.cheby1(N, Rp, Wn, btype=passband.value, analog=True, )

        elif protoTypes == ProtoType.CHEBYSHEV2:
            N, Wn = signal.cheb2ord(wp, ws, Rp, As, analog=True)
            b, a = signal.cheby2(N, As, Wn, btype=passband.value, analog=True)
        else:
            N, Wn = signal.ellipord(wp, ws, Rp, As, analog=True)
            b, a = signal.ellip(N, Rp, As, Wn, btype=passband.value, analog=True)
        self.b, self.a = signal.bilinear(b, a, fs=sampleRate)

        self.filter = FilterType.FIR
        self.passband = passband
        self.sampleRate = sampleRate

        self.w, self.h = signal.freqz(self.b, self.a, worN=self.nfft)

    # 获取频率响应
    def getFreqz(self):
        return self.b, self.a, self.w, self.h, self.sampleRate, self.nfft
