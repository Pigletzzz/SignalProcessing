from PyQt5.QtWidgets import QWidget, QDesktopWidget
from qfluentwidgets import SplitFluentWindow, FluentIcon, NavigationAvatarWidget, NavigationItemPosition

from view.AudioAnalysisView import AudioAnalysisView
from view.AudioFilterView import AudioFilterView
from view.FilterDesignerView import FilterDesignerView
from view.HomeView import HomeView


class MainWindow(SplitFluentWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.homeView = HomeView()
        self.audioAnalysisView = AudioAnalysisView()
        self.filterDesignerView = FilterDesignerView()
        self.audioFilterView = AudioFilterView()

        self.resize(1200, 800)
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

    def initNavigation(self):
        self.addSubInterface(self.homeView, FluentIcon.HOME, '首页')
        self.addSubInterface(self.audioAnalysisView, FluentIcon.MICROPHONE, '语音分析')
        self.addSubInterface(self.filterDesignerView, FluentIcon.VIDEO, '滤波器设计')
        self.addSubInterface(self.audioFilterView, FluentIcon.MEDIA, '语音滤波')

        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Pun-zeoncoeng', './resources/my_icon.png'),
            position=NavigationItemPosition.BOTTOM
        )

        self.navigationInterface.setExpandWidth(280)

    def route(self, index: QWidget):
        widget = self.stackedWidget.widget(index)
        self.switchTo(widget)
