import os

import soundfile
from scipy import signal

from model.AudioModel import AudioModel
from model.FilterModel import FilterModel


class AudioFilterPresenter:
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

        # 画图
        self.audioFilterView.plotProcessedAudio(y, audio.sampleRate)
        self.audioFilterView.plotOriginAudio(audio.voiceNum, audio.sampleRate)

        # 导出滤波后的文件，方便播放
        try:
            if not os.path.exists('./output'):
                os.mkdir('./output')
            title = audio.title.split('.')[0] + '.wav'
            soundfile.write('./output/' + title, y, audio.sampleRate)
            self.audioFilterView.setPlayer('./output/' + title)
        except Exception as e:
            print(e)

    def getCurrentAudioInfo(self, index: int):
        audio = self.audioModel.getAudio(index)
        return audio.sampleRate
