"""This file is only fo building app. All app-wide settings is in windows.app"""

from kivy.lang.builder import Builder

from app.build import BuildApp

kv = Builder.load_file("main.kv")

if __name__ == "__main__":
    BuildApp().run()
