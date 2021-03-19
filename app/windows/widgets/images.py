from kivy.uix.image import Image


class TwoStateClickableImage(Image):
    state = 1

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.state == 1:
                self.source = "static/no.png"
                self.state = 0
            else:
                self.source = "static/yes.png"
                self.state = 1


class WaitForResultsImage(Image):
    anim_delay = 0.1
    anim_loop = 5
    size_hint = (0.1, 0.1)

    def __init__(self, **kwargs):
        super(WaitForResultsImage, self).__init__(**kwargs)
