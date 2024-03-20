import os.path

import librosa

from model.VoiceModel import VoiceModel
from entity.voice import Voice


class VoiceFileController:
    def __init__(self, voiceAnalysisView, voiceModel: VoiceModel):
        self.voiceAnalysisView = voiceAnalysisView
        self.voiceModel = voiceModel

    # 读取音频文件
    def readFile(self, fileName):
        # 使用pydub读取音频文件
        y, sr = librosa.load(fileName)
        # 这里可以添加更多的音频处理逻辑
        voice = Voice(y, os.path.basename(fileName), int(len(y) / sr), os.path.dirname(fileName), int(sr),
                      os.path.getsize(fileName))
        self.addFile(voice)

    def addFile(self, voice: Voice):
        # 在model中添加项
        self.voiceModel.addVoice(voice)
        # 为view中的table添加一项
        self.voiceAnalysisView.addTabItem(voice)

    def selectFile(self, index: int):
        self.voiceAnalysisView.setupVoice(self.voiceModel.getVoice(index))
