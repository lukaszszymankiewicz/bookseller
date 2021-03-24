from kivy.uix.image import Image


class WaitForResultsImage(Image):
    anim_delay = 0.1
    anim_loop = 5
    size_hint = (0.1, 0.1)

    def __init__(self, **kwargs):
        super(WaitForResultsImage, self).__init__(**kwargs)
