from pydub import AudioSegment


class Voice(object):
    def __init__(self, audio, title, duration, path, bitRate, size):
        # AudioSegment实例对象
        self.audio: AudioSegment = audio
        # 文件名
        self.title: str = title
        # 时长 单位ms
        self.duration: int = duration
        # 文件路径
        self.path: str = path
        # 比特率 单位kbps
        self.bitRate: int = bitRate
        # 文件大小
        self.size: int = size
