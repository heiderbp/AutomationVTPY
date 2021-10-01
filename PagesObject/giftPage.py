from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.Locators import Locators


class giftPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Gift Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.submenuActivate = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "1").replace("MENU", "5"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Activate: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuInquiry = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "2").replace("MENU", "5"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Inquiry: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuReload = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "3").replace("MENU", "5"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Reload: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickSubmenu(self, name):
        error = list()
        fill = dict()
        method = "Deshboard Button: " + name

        if name == "Activate":
            submenu = self.submenuActivate
        elif name == "Inquiry":
            submenu = self.submenuInquiry
        elif name == "Reload":
            submenu = self.submenuReload
        else:
            submenu = " "
            print("Submenu not found")

        error += self.help.click_button(self.page, submenu)

        if len(error) == 0:
            self.help.info_log(self.page, "Successfully clicked in " + name)
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill