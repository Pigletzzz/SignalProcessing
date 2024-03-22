from entity.Audio import Audio


class AudioModel:
    def __init__(self):
        self.audios: list = []

    def addAudio(self, audio: Audio):
        self.audios.append(audio)

    def getAudio(self, index: int):
        return self.audios[index]
