import sys

from PyQt5.QtWidgets import QApplication

from controller.route_controller import RouteController
from controller.voice_file_controller import VoiceFileController
from model.VoiceModel import VoiceModel
from view.main_window_view import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()

    voiceModel = VoiceModel()

    routeController = RouteController(myWin)
    voiceFileController = VoiceFileController(myWin.voiceAnalysisView, voiceModel)

    myWin.homeView.routeController = routeController
    myWin.voiceAnalysisView.voiceFileController = voiceFileController

    myWin.show()
    sys.exit(app.exec_())
