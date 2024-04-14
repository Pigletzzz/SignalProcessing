from scipy import signal

from model.AudioModel import AudioModel
from model.FilterModel import FilterModel


class AudioFilterController:
    def __init__(self, audioFilterView, audioModel: AudioModel, filterModel: FilterModel):
        self.audioFilterView = audioFilterView
        self.audioModel = audioModel
        self.filterModel = filterModel

    def audioFilter(self, indexes):
        # 检查是否导入音频
        if len(self.audioModel.audios) == 0:
            print("请先导入音频文件")
            return
        # 检查是否选择音频
        if len(indexes) == 0:
            print("请选择需要滤波的音频文件")
            return
        # 检查是否已生成滤波器
        if self.filterModel.filter is None:
            print("请先设计一个滤波器")
            return

        # 进行滤波
        audio = self.audioModel.getAudio(indexes[0].row())
        b, a = self.filterModel.b, self.filterModel.a
        y = signal.filtfilt(b, a, audio.voiceNum)
        self.audioFilterView.plotAudio(audio.voiceNum, y, audio.sampleRate)
