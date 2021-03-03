from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.size = (360, 640)

kv = Builder.load_file("main.kv")

from windows import BuildApp

if __name__ == "__main__":
    BuildApp().run()
