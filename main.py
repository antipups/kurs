from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text='Кнопка')


if __name__ == '__main__':
    MyApp().run()
