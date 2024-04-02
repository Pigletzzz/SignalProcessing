from entity.Filter import PassbandType, WindowType, ProtoType
from model.FilterModel import FilterModel


# 用于执行滤波相关操作的Controller
class FilterController(object):
    def __init__(self, filterDesignerView, filterModel: FilterModel):
        self.filterDesignerView = filterDesignerView
        self.filterModel = filterModel
        self.passbands = [PassbandType.LOWPASS, PassbandType.HIGHPASS, PassbandType.BANDPASS, PassbandType.BANDSTOP]
        self.windows = [WindowType.BOXCAR, WindowType.TRIANG, WindowType.HANNING, WindowType.HAMMING,
                        WindowType.BLACKMAN, WindowType.KAISER]
        self.protoTypes = [ProtoType.BUTTERWORTH, ProtoType.CHEBYSHEV1, ProtoType.CHEBYSHEV2, ProtoType.ELLIPSE]

    # Fir滤波器设计方法
    def firDesign(self, sampleRate: str, order: str, cutoffFreq1: str, cutoffFreq2: str, passband: int, window: int):
        if len(sampleRate) == 0 or len(order) == 0 or len(cutoffFreq1) == 0 or passband == -1 or window == -1 or (
                passband > 1 and len(cutoffFreq2) == 0):
            self.filterDesignerView.onFailedInfo('缺少必要的参数')
            return

        # 打印信息
        print("\n------FIR Filter Design------")
        print('Passband: ' + self.passbands[passband].value)
        print('SampleRate: ' + sampleRate + 'Hz')
        print('CutoffFrequency: ' + cutoffFreq1 + 'Hz')
        if passband > 1:
            print('CutoffFrequency: ' + cutoffFreq2 + 'Hz')
        print('Order: ' + order)
        print('Window: ' + self.windows[window].value + '')

        try:
            # 处理可能未填写的高频率
            if passband < 2:
                cutoffFreqHigh = 0
            else:
                cutoffFreqHigh = int(cutoffFreq2)
            # 调用filterModel的fir设计方法进行fir滤波器设计
            self.filterModel.firDesign(int(sampleRate), int(cutoffFreq1), cutoffFreqHigh, self.passbands[passband],
                                       int(order), self.windows[window])
            print("Successfully!\n")
            # 成功，调用view的方法更新图表
            # print(str())
            b, a, w, h, fs, nfft = self.filterModel.getFreqz()
            self.filterDesignerView.onPlotUpdate(b, a, w, h, fs, nfft)
        except ValueError as e:
            # 弹出弹窗
            self.filterDesignerView.onFailedInfo(str(e))
            print(e)

    def iirDesign(self, sampleRate: str, passbandLow: str, passband1: str, stopbandLow: str, stopband1: str,
                  passbandRipple: str, stopbandAttenuation: str, passband: int, protoType: int):
        if len(sampleRate) == 0 or len(passbandLow) == 0 or len(stopbandLow) == 0 or len(passbandRipple) == 0 or len(
                stopbandAttenuation) == 0 or passband == -1 or protoType == -1 or (
                passband > 1 and (len(passband1) == 0 or len(stopband1) == 0)):
            self.filterDesignerView.onFailedInfo('缺少必要的参数')
            return

        # 打印信息
        print("\n------IIR Filter Design------")
        print('Passband: ' + self.passbands[passband].value)
        print('SampleRate: ' + sampleRate + 'Hz')
        print('PassbandFrequency: ' + passbandLow + 'Hz')
        if passband > 1:
            print('PassbandFrequency: ' + passband1 + 'Hz')
        print('StopbandFrequency: ' + stopbandLow + 'Hz')
        if passband > 1:
            print('StopbandFrequency: ' + stopband1 + 'Hz')
        print('PassbandRipple: ' + passbandRipple + 'dB')
        print('StopbandAttenuatio: ' + stopbandAttenuation + 'dB')
        print('ProtoType: ' + self.protoTypes[protoType].value)

        try:
            # 处理可能未填写的高频率
            if passband < 2:
                passbandHigh = 0
                stopbandHigh = 0
            else:
                passbandHigh = int(passband1)
                stopbandHigh = int(stopband1)
            # 调用filterModel的iir设计方法进行iir滤波器设计
            self.filterModel.iirDesign(int(sampleRate), int(passbandLow), passbandHigh, int(stopbandLow), stopbandHigh,
                                       float(passbandRipple), float(stopbandAttenuation), self.passbands[passband],
                                       self.protoTypes[protoType])
            print("Successfully!\n")
            # 成功，调用view的方法更新图表
            # print(str())
            b, a, w, h, fs, nfft = self.filterModel.getFreqz()
            self.filterDesignerView.onPlotUpdate(b, a, w, h, fs, nfft)
        except ValueError as e:
            # 弹出弹窗
            self.filterDesignerView.onFailedInfo(str(e))
            print(e)

    def updatePlot(self):
        print('update')
