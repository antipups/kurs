import re
import threading
import animation1
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


class AlfabInput(TextInput):    # переписанный текст инпут, для того чтоб вводили только a b или c

    pat = re.compile('[^a-c]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(AlfabInput, self).insert_text(s, from_undo=from_undo)


class MyApp(App):
    def build(self):
        def create_window(instance):
            if not text_input.text or text_input.text.find('.') > -1:
                text_input.text = ''
                text_input.hint_text_color = [1, 0, 0, 1]
                text_input.hint_text = 'Введите НОРМАЛЬНОЕ слово.'
                return
            text_input.text, text_input.foreground_color = functional.run(0, text_input.text)
        box_layout = BoxLayout(orientation='vertical')
        text_input = AlfabInput(hint_text="Введите желаемое слово:",
                                multiline=False,
                                on_text_validate=create_window,
                                )
        text_input.focus = True
        button = Button(text='Проверить',
                        on_release=create_window)
        box_layout.add_widget(text_input)
        box_layout.add_widget(button)
        return box_layout


if __name__ == '__main__':
    open('sample.txt', 'w').close()     # пересоздаем файл
    threading.Thread(target=functional.generate, daemon=True).start()   # создаем в отдельном потоке генератор
    threading.Thread(target=animation1.draw, daemon=True).start()       # создаем в отдельном потоке прорисовку временной трудности
    MyApp().run()
