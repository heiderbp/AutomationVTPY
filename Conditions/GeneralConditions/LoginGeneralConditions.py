import unittest

from Configurations.LoadWebDriver import LoadWebDriver
from Helpers.Helps import Helps


class loginGC(unittest.TestCase):
    driver = None
    help = Helps()
    name_test = str()
    page = str()
    error = str()
    mid = help.get_parameters()["mid"]["standard"]
    user = help.get_parameters()["users"]["standard"]
    password = help.get_parameters()["passwords"]["standard"]

    @classmethod
    def setUpClass(cls) -> None:
        cls.sel = LoadWebDriver(cls.help)
        cls.driver = cls.sel.driver
        cls.driver.get(cls.help.get_url())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
