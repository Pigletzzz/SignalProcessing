class RouteController:
    def __init__(self, main_window):
        self.main_window = main_window

    def routeToView(self, index: int):
        self.main_window.route(index)
