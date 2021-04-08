from os import path, makedirs
from datetime import datetime
from shutil import copy2

BACK_UP_PATH = 'e:\\backup'
BASE_NAME = '1Cv8.1CD'
DIRS_FROM_BACK_UP = ['e:\\base\\base1', 'e:\\base\\base2', 'e:\\base\\base3']


class BackUp:
    """
    class to perform back up 1c base from list dirs
    """

    def __init__(self, back_up_path=BACK_UP_PATH):
        self.back_up_path = path.join(back_up_path)

    def do_back_up(self):
        if not path.exists(path.join(BACK_UP_PATH)):
            makedirs(path.join(BACK_UP_PATH))
        for dir in DIRS_FROM_BACK_UP:
            file_name_src = path.join(dir, BASE_NAME)
            file_name_dst = self.get_file_name(dir)
            path_dst = path.join(BACK_UP_PATH, file_name_dst)
            try:
                copy2(file_name_src, path_dst)
            except FileNotFoundError as exp:
                print(exp)

    def get_file_name(self, dir):
        cur_datetime = datetime.today().strftime('%d-%m-%Y-%H-%M')
        name_dir = dir.split('\\')[-1]
        file_name = f'{name_dir}-{cur_datetime}.1CD'
        return file_name



if __name__ == '__main__':
    back_up = BackUp()
    back_up.do_back_up()
