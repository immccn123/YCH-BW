"""
A tool for Onion School to do the homework automatically.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from . import yangcong_tools

class YCHBW(toga.App):

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
        self.password_input = toga.TextInput(style=Pack(flex=1))

        password_box = toga.Box(style=Pack(direction=ROW, padding=5))
        password_box.add(password_label)
        password_box.add(self.password_input)

        button = toga.Button(
            "Go!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(username_box)
        main_box.add(password_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    
    def say_hello(self, widget):
        yangcong_tools.exec(self.username_input, self.password_input)

def main():
    return YCHBW()
