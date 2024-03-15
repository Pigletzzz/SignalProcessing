import sys

from PyQt5.QtWidgets import QApplication
from dotenv.parser import Position

from interface.filter_designer_interface import FilterDesignerInterface
from interface.home_interface import HomeInterface

from qfluentwidgets import SplitFluentWindow, FluentIcon, NavigationAvatarWidget, NavigationItemPosition

from interface.voice_analysis_interface import VoiceAnalysisInterface
from interface.voice_filter_interface import VoiceFilterInterface


class Window(SplitFluentWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Signal Processing')
        # self.setWindowIcon(QIcon(''))

        self.homeInterface = HomeInterface()
        self.voiceAnalysisInterface = VoiceAnalysisInterface()
        self.filterDesignerInterface = FilterDesignerInterface()
        self.voiceFilterInterface = VoiceFilterInterface()
        self.addSubInterface(self.homeInterface, FluentIcon.HOME, '首页')
        self.addSubInterface(self.voiceAnalysisInterface, FluentIcon.MICROPHONE, '语音分析')
        self.addSubInterface(self.filterDesignerInterface, FluentIcon.VIDEO, '滤波器设计')
        self.addSubInterface(self.voiceFilterInterface, FluentIcon.MEDIA, '语音滤波')

        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Pun-zeoncoeng', './resource/my_icon.png'),
            position=NavigationItemPosition.BOTTOM
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Window()
    myWin.show()
    sys.exit(app.exec_())
