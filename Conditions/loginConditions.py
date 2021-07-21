import unittest

from selenium import webdriver

from Conditions.GeneralConditions.LoginGeneralConditions import loginGC
from Helpers.Helps import Helps


class LoginConditions(loginGC):

    def setUp(self) -> None:
        self.driver.refresh()

    def tearDown(self) -> None:
        self.help.tear_down(self.name_test, self.page, self.error, self.mid)