from random import randint

from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')

class MyFirstApp(App):

    def btn_press(self, instance):
        instance.text = "Новое число: " + str(randint(1, 100))

    def build(self):
        return Button(text = "Привет! Нажми на меня,\nи я покажу новое число!",
        on_press = self.btn_press,
        size_hint = [0.5, 0.5], 
        pos = [600/2-600/4, 600/2-600/4])

if __name__ == "__main__":
    MyFirstApp().run()