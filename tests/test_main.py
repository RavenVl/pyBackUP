import unittest
from main import BackUp
import datetime
from freezegun import freeze_time




class TestBackUpMethod(unittest.TestCase):

    @freeze_time("2021-04-08 11:28")
    def test_upper(self):
        back_up = BackUp()
        fake_time = datetime.datetime.strptime('08-04-2021 11:28', '%d-%m-%Y %H:%M')
        dir_ = 'base1'

        self.assertEqual(back_up.get_file_name(dir_), 'base1-08-04-2021-11-28.1CD')


if __name__ == '__main__':
    unittest.main()
