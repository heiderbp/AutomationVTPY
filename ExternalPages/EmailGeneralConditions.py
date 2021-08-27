import unittest

from Configurations.LoadWebDriver import LoadWebDriver
from Helpers.Helps import Helps


class emailGC(unittest.TestCase):
    driver = None
    help = Helps()
    name_test = str()
    page = str()
    error = str()


    @classmethod
    def setUpClass(cls) -> None:
        cls.sel = LoadWebDriver(cls.help)
        cls.driver = cls.sel.driver
        cls.driver.get(cls.help.get_url_email())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
