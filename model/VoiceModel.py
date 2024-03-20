from entity.voice import Voice


class VoiceModel:
    def __init__(self):
        self.voices: list = []

    def addVoice(self, voice: Voice):
        self.voices.append(voice)

    def getVoice(self, index: int):
        return self.voices[index]
