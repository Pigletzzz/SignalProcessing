from pydub import AudioSegment


class Voice(object):
    def __init__(self, audio, title, duration):
        # AudioSegment实例对象
        self.audio: AudioSegment = audio
        # 文件名
        self.title: str = title
        # 时长 单位ms
        self.duration: int = duration
