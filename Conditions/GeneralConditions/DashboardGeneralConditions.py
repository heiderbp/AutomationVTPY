import unittest

from Configurations.LoadWebDriver import LoadWebDriver
from Helpers.Helps import Helps
from PagesObject.Pages.loginPage import LoginPage


class dashboardGC(unittest.TestCase):
    driver = None
    help = Helps()
    name_test = str()
    page = str()
    error = str()
   # mid = help.get_parameters()["mid"]["standard"]
   # user = help.get_parameters()["users"]["standard"]
   # password = help.get_parameters()["passwords"]["standard"]

    @classmethod
    def setUpClass(cls) -> None:
        cls.sel = LoadWebDriver(cls.help)
        cls.driver = cls.sel.driver
        cls.driver.get(cls.help.get_url())
       # login = LoginPage(cls.driver, cls.help)
       # login.fillFrom(cls.user, cls.password, cls.mid)
       # login.clicksubmitLogin()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
