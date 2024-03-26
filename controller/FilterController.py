from entity.Filter import PassbandType, WindowType
from model.FilterModel import FilterModel


# 用于执行滤波相关操作的Controller
class FilterController(object):
    def __init__(self, filterDesignerView, filterModel: FilterModel):
        self.filterDesignerView = filterDesignerView
        self.filterModel = filterModel

    # Fir滤波器设计方法
    def firDesign(self, sampleRate, order, cutoffFreq):
        # TODO 判断输入合法性
        self.filterModel.firDesign(sampleRate, cutoffFreq, PassbandType.LOWPASS, order, WindowType.BOXCAR)

    def updatePlot(self):
        print('update')
