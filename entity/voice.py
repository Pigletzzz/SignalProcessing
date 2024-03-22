import numpy


class Voice(object):
    def __init__(self, voiceNum: numpy.ndarray, title: str, duration: int, path: str, sampleRate: int, size: int):
        # AudioSegment实例对象
        self.voiceNum: numpy.ndarray = voiceNum
        # 文件名
        self.title: str = title
        # 时长 单位ms
        self.duration: int = duration
        # 文件路径
        self.path: str = path
        # 比特率 单位kbps
        self.sampleRate: int = sampleRate
        # 文件大小
        self.size: int = size
