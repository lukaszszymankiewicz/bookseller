from kivy.uix.label import Label


class CenteredLabel(Label):
    font_size = 20
    size_hint = (0.5, 0.1)

    def __init__(self, **kwargs):
        super(CenteredLabel, self).__init__(**kwargs)
