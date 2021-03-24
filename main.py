from kivy.lang.builder import Builder

from app.build import BuildApp

kv = Builder.load_file("app.kv")

if __name__ == "__main__":
    BuildApp().run()
