from multiprocessing import Process
from queue import Queue

import toga

from . import yangcong_tools

message_queue = Queue(10)
homework_th = Process()
message_th = Process()


def run_homework(self: toga.App):
    global message_queue, homework_th, message_th
    print(self.username_input.value, self.password_input.value)

    homework_th = Process(
        target=yangcong_tools.exec,
        args=[
            self.username_input.value,
            self.password_input.value,
            message_queue,
        ])

    message_th = Process(
        target=self.get_message,
        args=[self],
    )

    homework_th.start()
    message_th.start()
