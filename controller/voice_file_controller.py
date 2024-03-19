import os.path

from pydub import AudioSegment

from model.VoiceModel import VoiceModel
from entity.voice import Voice


class VoiceFileController:
    def __init__(self, voiceAnalysisView, voiceModel: VoiceModel):
        self.voiceAnalysisView = voiceAnalysisView
        self.voiceModel = voiceModel

    # 读取音频文件
    def readFile(self, fileName):
        # 使用pydub读取音频文件
        audio = AudioSegment.from_file(fileName, format=fileName.split('.')[-1])
        # 这里可以添加更多的音频处理逻辑
        voice = Voice(audio, os.path.basename(fileName), len(audio), os.path.dirname(fileName), audio.frame_rate,
                      os.path.getsize(fileName))
        self.addFile(voice)

    def addFile(self, voice: Voice):
        # 在model中添加项
        self.voiceModel.addVoice(voice)
        # 为view中的table添加一项
        self.voiceAnalysisView.addTabItem(voice)

    def selectFile(self, index: int):
        self.voiceAnalysisView.showVoice(self.voiceModel.getVoice(index))
