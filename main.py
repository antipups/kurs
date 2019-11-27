import re
import threading
import functional
from kivy.config import Config
Config.set('graphics', 'left', '28')
Config.set('graphics', 'top', '50')
Config.set('graphics', 'position', 'custom')
Config.set('kivy', 'exit_on_escape', '1')
Config.set('graphics', 'height', '70')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'resizable', '0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import animation1


class FloatInput(TextInput):    # переписанный текст инпут, для того чтоб вводили только a b или c

    pat = re.compile('[^a-c]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class MyApp(App):
    def build(self):
        def create_window(instance):
            threading.Thread(target=animation1.draw, daemon=True).start()
            text_input.text, text_input.foreground_color = functional.run(text_input.text)
        box_layout = BoxLayout(orientation='vertical')
        text_input = FloatInput(hint_text="Введите желаемое слово:",
                                multiline=False,
                                on_text_validate=create_window)
        button = Button(text='Проверить',
                        on_press=create_window)
        box_layout.add_widget(text_input)
        box_layout.add_widget(button)
        return box_layout


if __name__ == '__main__':
    MyApp().run()
