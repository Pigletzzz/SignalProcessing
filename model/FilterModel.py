import numpy as np
from scipy import signal

from entity.Filter import FilterType, PassbandType, WindowType, ProtoType


# 滤波器Model基类
class FilterModel(object):

    def __init__(self):
        self.h = None
        self.w = None
        self.passband = None
        self.sampleRate = None
        self.b = None
        self.a = None
        self.filter = None
        self.nfft = 4096
        self.cutoff = None

    def firDesign(self, sampleRate: int, cutoffFreq1, cutoffFreq2, passband: PassbandType, order: int,
                  window: WindowType):
        if passband == PassbandType.LOWPASS or passband == PassbandType.HIGHPASS:
            cutoffFreq = cutoffFreq1 / sampleRate
        else:
            cutoffFreq = [cutoffFreq1 / sampleRate, cutoffFreq2 / sampleRate]
        self.b = signal.firwin(order + 1, cutoffFreq, window=window.value, pass_zero=passband.value)
        self.a = 1

        self.cutoff = cutoffFreq
        self.filter = FilterType.FIR
        self.passband = passband
        self.sampleRate = sampleRate
        # self.filter = Filter(FilterType.FIR, sampleRate, passband, b, 1)

        # 求出频率响应
        self.w, self.h = signal.freqz(self.b, self.a, worN=self.nfft)

    def iirDesign(self, sampleRate: int, passbandLow: int, passbandHigh: int, stopbandLow: int, stopbandHigh: int,
                  Rp: float, As: float, passband: PassbandType, protoTypes: ProtoType):
        # 计算参数
        # TODO 频率预畸
        fn = sampleRate
        if (passband == PassbandType.LOWPASS or passband == PassbandType.HIGHPASS):
            wp = passbandLow * 2 * np.pi / sampleRate / 2  # 由于未知的原因，这里需要除二，否则生成的滤波器参数是输入值的两倍
            ws = stopbandLow * 2 * np.pi / sampleRate / 2
            p = 2 * sampleRate * np.tan(wp / 2)
            st = 2 * sampleRate * np.tan(ws / 2)
            self.cutoff = passbandLow / sampleRate
        else:
            wp = [passbandLow * 2 * np.pi / sampleRate / 2, passbandHigh * 2 * np.pi / sampleRate / 2]
            ws = [stopbandLow * 2 * np.pi / sampleRate / 2, stopbandHigh * 2 * np.pi / sampleRate / 2]
            p = [2 * sampleRate * np.tan(wp[0] / 2), 2 * sampleRate * np.tan(wp[1] / 2)]
            st = [2 * sampleRate * np.tan(ws[0] / 2), 2 * sampleRate * np.tan(ws[1] / 2)]
            self.cutoff = [passbandLow / sampleRate, passbandHigh / sampleRate]

        # 分别计算滤波器参数
        if protoTypes == ProtoType.BUTTERWORTH:
            print('Rp = ', Rp)
            print('As = ', As)
            N, Wn = signal.buttord(p, st, Rp, As, analog=True)
            b, a = signal.butter(N, Wn, btype=passband.value, analog=True)
        elif protoTypes == ProtoType.CHEBYSHEV1:
            N, Wn = signal.cheb1ord(p, st, Rp, As, analog=True)
            b, a = signal.cheby1(N, Rp, Wn, btype=passband.value, analog=True)

        elif protoTypes == ProtoType.CHEBYSHEV2:
            N, Wn = signal.cheb2ord(p, st, Rp, As, analog=True)
            b, a = signal.cheby2(N, As, Wn, btype=passband.value, analog=True)
        else:
            N, Wn = signal.ellipord(p, st, Rp, As, analog=True)
            b, a = signal.ellip(N, Rp, As, Wn, btype=passband.value, analog=True)
        self.b, self.a = signal.bilinear(b, a, fs=sampleRate)

        self.filter = FilterType.IIR
        self.passband = passband
        self.sampleRate = sampleRate

        # 获取频率响应
        self.w, self.h = signal.freqz(self.b, self.a, worN=self.nfft)

    def getFreqz(self):
        return self.b, self.a, self.w, self.h, self.sampleRate, self.nfft

    def getInfo(self):
        return self.filter, self.passband, self.sampleRate, self.cutoff
