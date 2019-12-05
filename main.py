import re
import threading
import time

import animation1
import functional
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
Config.set('graphics', 'left', '28')
Config.set('graphics', 'top', '50')
Config.set('graphics', 'position', 'custom')
Config.set('kivy', 'exit_on_escape', '1')
Config.set('graphics', 'height', '517')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'resizable', '0')


class AlfabInput(TextInput):    # переписанный текст инпут, для того чтоб вводили только a b или c
    pat = re.compile('[^a-c]')  # патерн, сюда вводим значения которые нам нужны

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(AlfabInput, self).insert_text(s, from_undo=from_undo)


class MyApp(App):
    def build(self):
        def run_the_task(instance):
            if not text_input.text or text_input.text.find('.') > -1:   # если введено что-то не то
                text_input.text = ''
                text_input.hint_text_color = [1, 0, 0, 1]
                text_input.hint_text = 'Введите НОРМАЛЬНОЕ слово.'
            else:
                for name_of_file in ('log.txt', 'multi_log.txt'):   # чистим файлы после прошлого запуска
                    open(name_of_file, 'w').close()
                text_input.hint_text, text_input.hint_text_color = \
                    functional.run(text_input.text, False, True if int(instance.id) == 1 else False)
                if int(instance.id) != 1:
                    name_of_file = 'log.txt'
                else:
                    name_of_file = 'multi_log.txt'
                with open(name_of_file, 'r') as f:
                    log_text_input.text = f.read()
                text_input.text = ''

        box_layout = BoxLayout(orientation='vertical')
        text_input = AlfabInput(hint_text="Введите желаемое слово:",
                                multiline=False,
                                on_text_validate=run_the_task,
                                id='0',
                                size_hint_y=.1)
        text_input.focus = True
        button = Button(text='Одноленточная',
                        on_release=run_the_task,
                        id='0',
                        size_hint_y=.1)
        button_multi = Button(text='Многоленточная',
                              on_release=run_the_task,
                              id='1',
                              size_hint_y=.1)
        log_text_input = TextInput(hint_text='Тут будут логи машин.',
                                   readonly=False)
        box_layout.add_widget(text_input)
        box_layout.add_widget(button)
        box_layout.add_widget(button_multi)
        box_layout.add_widget(log_text_input)
        return box_layout


if __name__ == '__main__':
    for name_of_file in ('time.txt', 'multi_time.txt'):     # чистим файлы с графиками
        open(name_of_file, 'w').close()
    threading.Thread(target=functional.generate, daemon=True).start()   # создаем в отдельном потоке генератор
    threading.Thread(target=animation1.draw, daemon=True).start()       # создаем в отдельном потоке прорисовку временной трудности
    MyApp().run()   # запускаем основное окно с основной задачей
