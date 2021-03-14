from kivy.uix.screenmanager import Screen


class BaseBooksellerWindow(Screen):
    orientation = "vertical"

    def __init__(self, **kwargs):
        super(BaseBooksellerWindow, self).__init__(**kwargs)
