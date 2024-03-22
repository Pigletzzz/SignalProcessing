import os.path

import librosa

from entity.Audio import Audio
from model.AudioModel import AudioModel


class AudioFileController:
    def __init__(self, voiceAnalysisView, audioModel: AudioModel):
        self.voiceAnalysisView = voiceAnalysisView
        self.audioModel = audioModel

    # 读取音频文件
    def readFile(self, fileName):
        # 使用pydub读取音频文件
        y, sr = librosa.load(fileName, sr=None)
        # 这里可以添加更多的音频处理逻辑
        voice = Audio(y, os.path.basename(fileName), int(len(y) / sr), os.path.dirname(fileName), int(sr),
                      os.path.getsize(fileName))
        self.addFile(voice)

    def addFile(self, voice: Audio):
        # 在model中添加项
        self.audioModel.addAudio(voice)
        # 为view中的table添加一项
        self.voiceAnalysisView.addTabItem(voice)

    def selectFile(self, index: int):
        self.voiceAnalysisView.setupVoice(self.audioModel.getAudio(index))
