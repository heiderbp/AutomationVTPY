from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.Locators import Locators


class cardPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Cards Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.submenuSale = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "1").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Sale: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuUseToken = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "2").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Use Token: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuRefund = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "3").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Refund: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuAuth = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "4").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Auth: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuForce = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "5").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Force: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuVoice = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "6").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Voice: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuCredit = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "7").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Credit: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuPositiveCard = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "8").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Positive Cards: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuManageToken = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "9").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Manage Token: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuBatchDeposit = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "10").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Batch Deposit: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuLevelIII = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "11").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Level III: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuLightRecurring = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "12").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Light Recurring: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuReAuth = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "13").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item ReAuth: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuEBPPInvoice = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "14").replace("MENU", "3"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item EBPP Invoice: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickSubmenu(self, name):
        error = list()
        fill = dict()
        method = "Desboard Button: " + name

        if name == "Sale":
            submenu = self.submenuSale
        elif name == "UseToken":
            submenu = self.submenuUseToken
        elif name == "Refund":
            submenu = self.submenuRefund
        elif name == "Auth":
            submenu = self.submenuAuth
        elif name == "Force":
            submenu = self.submenuForce
        elif name == "Voice":
            submenu = self.submenuVoice
        elif name == "Credit":
            submenu = self.submenuCredit
        elif name == "PositiveCard":
            submenu = self.submenuPositiveCard
        elif name == "ManageToken":
            submenu = self.submenuManageToken
        elif name == "BatchDeposit":
            submenu = self.submenuBatchDeposit
        elif name == "LevelIII":
            submenu = self.submenuLevelIII
        elif name == "LightRecurring":
            submenu = self.submenuLightRecurring
        elif name == "ReAuth":
            submenu = self.submenuReAuth
        elif name == "EBPPInvoice":
            submenu = self.submenuEBPPInvoice
        else:
            submenu = " "
            print("Submenu not found")

        error += self.help.click_button(self.page, submenu)

        if len(error) == 0:
            self.help.info_log(self.page, "Successfully clicked " + name)
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill