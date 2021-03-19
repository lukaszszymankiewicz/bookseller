from kivy.uix.gridlayout import GridLayout


class FullWidthGridLayoutThin(GridLayout):
    size_hint = (0.8, 0.1)

    def __init__(self, **kwargs):
        super(FullWidthGridLayoutThin, self).__init__(**kwargs)


class FullWidthGridLayoutChunky(GridLayout):
    size_hint = (0.5, 0.3)

    def __init__(self, **kwargs):
        super(FullWidthGridLayoutChunky, self).__init__(**kwargs)


class FullWidthGridLayoutChunkiest(GridLayout):
    size_hint = (0.8, 0.5)

    def __init__(self, **kwargs):
        super(FullWidthGridLayoutChunkiest, self).__init__(**kwargs)
