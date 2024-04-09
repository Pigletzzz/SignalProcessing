from enum import Enum


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


# 窗函数类型枚举
class WindowType(Enum):
    BOXCAR = 'boxcar'
    TRIANG = 'triang'
    HANNING = 'hann'
    HAMMING = 'hamming'
    BLACKMAN = 'blackmanharris'
    KAISER = 'kaiser'


class ProtoType(Enum):
    BUTTERWORTH = 'Butterworth'
    CHEBYSHEV1 = 'Chebyshev-1'
    CHEBYSHEV2 = 'Chebyshev-2'
    ELLIPSE = 'Ellipse'
