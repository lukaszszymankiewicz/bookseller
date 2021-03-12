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
