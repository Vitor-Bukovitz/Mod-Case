from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.graphics import *
from kivy.clock import Clock
from kivy.config import Config
import time

LabelBase.register(name="Quicksand", fn_regular="Quicksand-Regular.otf")
Window.fullscreen = 'auto'

class Menu(Screen):
    pass

class ClockText(Label):
    def update(self, *args):
        self.text = time.asctime()
        return ClockText

class Mod_Case(App):
    def build(self):
        main_menu = Menu()
        clocktext = main_menu.ids.clocktext
        Clock.schedule_interval(clocktext.update, 1)  

        return main_menu


if __name__ == "__main__":
    Mod_Case().run()