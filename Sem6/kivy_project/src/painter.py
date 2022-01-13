from random import randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.core.window import Window


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def red_mode(self, instance):
        self.painter.canvas.add(Color(1, 0, 0))

    def green_mode(self, instance):
        self.painter.canvas.add(Color(0, 1, 0))

    def blue_mode(self, instance):
        self.painter.canvas.add(Color(0, 0, 1))
    
    def random_mode(self, instance):
        self.painter.canvas.add(Color(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255))

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        parent = Widget()
        self.painter = MyPaintWidget()
        self.painter.canvas.add(Color(0, 0, 0))
        btnsbox = BoxLayout(size_hint = (1, 0.2))

        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)

        redbtn = Button(text = 'Red Color', on_press = self.red_mode)
        greenbtn = Button(text = 'Green Color', on_press = self.green_mode)
        bluebtn = Button(text = 'Blue Color', on_press = self.blue_mode)
        randombtn = Button(text = 'Random Color', on_press = self.random_mode)

        parent.add_widget(self.painter)
        btnsbox.add_widget(clearbtn)
        btnsbox.add_widget(redbtn)
        btnsbox.add_widget(greenbtn)
        btnsbox.add_widget(bluebtn)
        btnsbox.add_widget(randombtn)

        window = BoxLayout(orientation = 'vertical')
        
        window.add_widget(parent)
        window.add_widget(btnsbox)
        return window

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
        self.painter.canvas.add(Color(0, 0, 0))


if __name__ == '__main__':
    MyPaintApp().run()