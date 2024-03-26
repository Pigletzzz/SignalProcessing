from scipy import signal

from entity.Filter import Filter, FilterType, PassbandType, WindowType


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
        self.filter = None

    def firDesign(self, sampleRate: int, cutoffFreq, passband: PassbandType, order: int, window: WindowType):
        # TODO 处理输入数据异常
        b = signal.firwin(order + 1, cutoffFreq / sampleRate, window=window.value, pass_zero=passband.value)
        self.filter = Filter(FilterType.FIR, sampleRate, passband, b, 1)

    def plot(self):
        if self.filter is None:
            # TODO 处理异常
            print("你还没有生成滤波器")
        else:
            # 幅度响应
            print("11")
