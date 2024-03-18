from entity.voice import Voice


class VoiceModel:
    def __init__(self):
        self.voices = []

    def addVoice(self, voice: Voice):
        self.voices.append(voice)

    def getVoices(self):
        return self.voices
