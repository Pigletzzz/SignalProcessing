class RouteController:
    def __init__(self, main_window, widgets):
        self.main_window = main_window
        self.widgets = widgets

    def routeToView(self, index: int):
        self.main_window.route(index)
