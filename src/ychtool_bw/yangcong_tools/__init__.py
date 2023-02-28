import time

from . import main


def exec(username, password, message_queue):
    print(username, password, message_queue)
    main.login(username, password)
    main.run(message_queue)
