from app.windows.ux.colors import WHITE
from kivy.uix.label import Label


class BaseLabel(Label):
    font_size = 20

    def __init__(self, **kwargs):
        super(BaseLabel, self).__init__(**kwargs)


class CenteredLabel(BaseLabel):
    color = WHITE
    size_hint = (0.5, 0.1)
    background_color = WHITE
    background_normal = ""
    multiline = False

    def __init__(self, **kwargs):
        super(CenteredLabel, self).__init__(**kwargs)
