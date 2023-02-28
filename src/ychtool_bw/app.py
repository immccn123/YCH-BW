"""
A tool for Onion School to do the homework automatically.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from . import homework_th, message_queue, message_th, run_homework

flag = 0


class YCHBW(toga.App):
    def get_message(self, *_):
        global homework_th
        while homework_th.is_alive():
            msg = message_queue.get()
            self.log_case.value += msg

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        username_label = toga.Label(
            "用户名: ",
            style=Pack(padding=(0, 5))
        )
        self.username_input = toga.TextInput(style=Pack(flex=1))

        username_box = toga.Box(style=Pack(direction=ROW, padding=5))
        username_box.add(username_label)
        username_box.add(self.username_input)

        password_label = toga.Label(
            "密码: ",
            style=Pack(padding=(0, 5))
        )
        self.password_input = toga.PasswordInput(style=Pack(flex=1))

        password_box = toga.Box(style=Pack(direction=ROW, padding=5))
        password_box.add(password_label)
        password_box.add(self.password_input)

        button = toga.Button(
            "Go!",
            on_press=self.deal_honework,
            style=Pack(padding=5),
        )

        log_box = toga.Box(style=Pack(direction=ROW, padding=5))
        self.log_case = toga.MultilineTextInput(
            "日志",
            style=Pack(flex=5),
            readonly=True,
        )

        log_box.add(self.log_case)

        main_box.add(username_box)
        main_box.add(password_box)
        main_box.add(button)
        main_box.add(log_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()



def main():
    return YCHBW()
