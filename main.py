from os import path
BACK_UP_PATH = 'e:\\backup'

DIRS_FROM_BACK_UP = ['e:\\base\\base1', 'e:\\base\\base2', 'e:\\base\\base3']

class BackUp:
    '''
    class to perform back up 1c base from list dirs
    '''
    def __init__(self, back_up_path = BACK_UP_PATH):
        self.back_up_path = path(back_up_path)

    def do_back_up(self):


if __name__ == '__main__':
