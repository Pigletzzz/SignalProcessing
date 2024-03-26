from enum import Enum

from scipy import signal


# 滤波器类别枚举
class FilterType(Enum):
    FIR = 0
    IIR = 1


# 通带类型枚举
class PassbandType(Enum):
    LOWPASS = 'lowpass'
    HIGHPASS = 'highpass'
    BANDPASS = 'bandpass'
    BANDSTOP = 'bandstop'


# 响应函数枚举
class ResponseType(Enum):
    BANDPASS = 'bandpass'
    BANDSTOP = 'bandstop'


# 窗函数类型枚举
class WindowType(Enum):
    BOXCAR = 'boxcar'
    TRIANG = 'triang'
    HANNING = 'hann'
    HAMMING = 'hamming'
    BLACKMAN = 'blackmanharris'
    KAISER = 'kaiser'


# Filter实例，用于存储滤波器滤波器的相关信息
class Filter(object):
    def __init__(self, filterType: FilterType, sampleRate: int, passband: PassbandType, b, a):
        self.sampleRate = sampleRate
        self.filterType = filterType
        self.passband = passband
        self.b = b
        self.a = a

        print('b = ' + str(b))
        print('a = ' + str(a))

        # 求出频率响应
        self.w, self.h = signal.freqz(self.b, self.a, worN=4096)

    def getFreqz(self):
        return self.w, self.h
