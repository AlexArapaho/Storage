from view import UserInterface


class Controller:
    def __init__(self):
        self.interface = UserInterface()

    def run(self):
        answer = None

        while answer != 'q':
            self.interface.wait_answer()
            self.


