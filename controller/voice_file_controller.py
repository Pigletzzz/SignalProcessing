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
        print(f"Duration in milliseconds: {len(audio)}")
        # 这里可以添加更多的音频处理逻辑
        voice = Voice(audio, fileName.split('/')[-1], len(audio))
        self.addFile(voice)
        # 在model中添加项
        self.voiceModel.addVoice(voice)

    # 为view中的table添加一项
    def addFile(self, voice: Voice):
        self.voiceAnalysisView.addTabItem(voice)
