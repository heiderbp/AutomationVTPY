from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.Locators import Locators


class checkPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Check Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.submenuGuarantee = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "1").replace("MENU", "4"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Guarantee: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuCheckConversion = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "2").replace("MENU", "4"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Check Conversion: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuManageToken = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "3").replace("MENU", "4"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Manage Token: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuUseToken = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "4").replace("MENU", "4"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Use Token: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuSendFile = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "5").replace("MENU", "4"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Send File: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuCOD = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "6").replace("MENU", "4"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item COD: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuVoid = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "7").replace("MENU", "4"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Void: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuHoldCheck = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "8").replace("MENU", "4"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Hold Check: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickSubmenu(self, name):
        error = list()
        fill = dict()
        method = "Desboard Button: " + name

        if name == "Guarantee":
            submenu = self.submenuGuarantee
        elif name == "CheckConversion":
            submenu = self.submenuCheckConversion
        elif name == "ManageToken":
            submenu = self.submenuManageToken
        elif name == "UseToken":
            submenu = self.submenuUseToken
        elif name == "SendFile":
            submenu = self.submenuSendFile
        elif name == "COD":
            submenu = self.submenuCOD
        elif name == "Void":
            submenu = self.submenuVoid
        elif name == "HoldCheck":
            submenu = self.submenuHoldCheck
        else:
            submenu = " "
            print("Submenu not found")

        error += self.help.click_button(self.page, submenu)

        if len(error) == 0:
            self.help.info_log(self.page, "Successfully clicked on " + name)
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill