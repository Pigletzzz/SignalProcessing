from PyQt5.QtWidgets import QWidget,QDesktopWidget
from qfluentwidgets import SplitFluentWindow, FluentIcon, NavigationAvatarWidget, NavigationItemPosition

from view.filter_designer_view import FilterDesignerView
from view.home_view import HomeView
from view.voice_analysis_view import VoiceAnalysisView
from view.voice_filter_view import VoiceFilterView


class MainWindow(SplitFluentWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.homeView = HomeView()
        self.voiceAnalysisView = VoiceAnalysisView()
        self.filterDesignerView = FilterDesignerView()
        self.voiceFilterView = VoiceFilterView()

        self.resize(800, 600)
        self.setWindowTitle('Signal Processing')
        # self.setWindowIcon(QIcon(''))
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft), int(newTop))

        self.initNavigation()

        self.widgets = [self.homeView, self.voiceAnalysisView,
                        self.filterDesignerView, self.voiceFilterView]

    def initNavigation(self):
        self.addSubInterface(self.homeView, FluentIcon.HOME, '首页')
        self.addSubInterface(self.voiceAnalysisView, FluentIcon.MICROPHONE, '语音分析')
        self.addSubInterface(self.filterDesignerView, FluentIcon.VIDEO, '滤波器设计')
        self.addSubInterface(self.voiceFilterView, FluentIcon.MEDIA, '语音滤波')

        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Pun-zeoncoeng', './resources/my_icon.png'),
            position=NavigationItemPosition.BOTTOM
        )

        self.navigationInterface.setExpandWidth(280)

    def route(self, index: QWidget):
        self.switchTo(self.widgets[index])
