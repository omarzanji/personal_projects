# Following the Kivy pong tutorial and noting basics of Kivy.
#
# Author: Omar Barazanji
# Date: 8/27/2020
# source: https://kivy.org/doc/stable/tutorials/pong.html

from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()

if __name__ == "__main__":
    PongApp().run()
