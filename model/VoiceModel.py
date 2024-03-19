from entity.voice import Voice


class VoiceModel:
    def __init__(self):
        self.voices: list = []

    def addVoice(self, voice: Voice):
        print(voice)
        self.voices.append(voice)
        print("voices count = " + str(len(self.voices)))

    def getVoice(self, index: int):
        return self.voices[index]
