from . import main

def exec(username, password):
    main.login(username, password)
    main.run()
