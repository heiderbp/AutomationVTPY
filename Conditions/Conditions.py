import unittest

from Configurations.LoadWebDriver import LoadWebDriver
from Helpers.Helps import Helps


class Conditions(unittest.TestCase):
    driver = None
    help = Helps()
    name_test = str()
    page = str()
    error = str()
    mid = str()

    @classmethod
    def setUpClass(cls) -> None:
        cls.sel = LoadWebDriver(cls.help)
        cls.driver = cls.sel.driver
        cls.driver.get(cls.help.get_url())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

    def setUp(self) -> None:
        self.driver.refresh()

    def tearDown(self) -> None:
        self.help.tear_down(self.name_test, self.page, self.error, self.mid)