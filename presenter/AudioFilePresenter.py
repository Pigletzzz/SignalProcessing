import os.path

import librosa

from entity.Audio import Audio
from model.AudioModel import AudioModel


class AudioFilePresenter:
    def __init__(self, audioAnalysisView, audioFilterView, audioModel: AudioModel):
        self.audioAnalysisView = audioAnalysisView
        self.audioFilterView = audioFilterView
        self.audioModel = audioModel

    # 读取音频文件
    def readFile(self, fileName):
        # 使用pydub读取音频文件
        y, sr = librosa.load(fileName, sr=None)
        # 这里可以添加更多的音频处理逻辑
        voice = Audio(y, os.path.basename(fileName), int(len(y) / sr), os.path.dirname(fileName), int(sr),
                      os.path.getsize(fileName))
        # 将对象存至Modal类内
        self.addFile(voice)
        # 回调画图
        self.audioAnalysisView.onPlotUpdate(y, sr)

    def addFile(self, audio: Audio):
        # 在model中添加项
        self.audioModel.addAudio(audio)
        # 为view中的table添加一项
        self.audioAnalysisView.addTabItem(audio)
        self.audioFilterView.addAudio(audio)

    def selectFile(self, index: int):
        audio = self.audioModel.getAudio(index)
        self.audioAnalysisView.setupAudio(audio)
        # 回调画图
        self.audioAnalysisView.onPlotUpdate(audio.voiceNum, audio.sampleRate)
