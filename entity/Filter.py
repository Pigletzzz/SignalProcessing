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
