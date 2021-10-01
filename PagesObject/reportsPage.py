from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.Locators import Locators


class reportsPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Reports Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.submenuReprint = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "1").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Reprint: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuTransactions = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "2").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Transactions: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuBatchReport = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "3").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Batch Report: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuSupervisor = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "4").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Supervisor: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuTransactionDistribution = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "5").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Transaction Distribution: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuLevelIIIData = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "6").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Level III Data: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuCustomFields = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "7").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Custom Fields: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuTokenSummary = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "8").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Token Summary: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuCheckReport = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "9").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Check Report: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuGeolocation = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "10").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Geolocation: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuIPSummary = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "11").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item IP Summary: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuEBPPReconciliation = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "12").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item EBPP Reconciliation: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuClientIDSummary = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "13").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Client ID Summary: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuCashSummary = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "14").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Cash Summary: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuDepartmentSummary = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "15").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Department Summary: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuDonationsSummary = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "16").replace("MENU", "6"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Donations Summary: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickSubmenu(self, name):
        error = list()
        fill = dict()
        method = "Desboard Button: " + name

        if name == "Reprint":
            submenu = self.submenuReprint
        elif name == "Transactions":
            submenu = self.submenuTransactions
        elif name == "BatchReport":
            submenu = self.submenuBatchReport
        elif name == "Supervisor":
            submenu = self.submenuSupervisor
        elif name == "TransactionDistribution":
            submenu = self.submenuTransactionDistribution
        elif name == "LevelIIIData":
            submenu = self.submenuLevelIIIData
        elif name == "CustomFields":
            submenu = self.submenuCustomFields
        elif name == "TokenSummary":
            submenu = self.submenuTokenSummary
        elif name == "CheckReport":
            submenu = self.submenuCheckReport
        elif name == "Geolocation":
            submenu = self.submenuGeolocation
        elif name == "IPSummary":
            submenu = self.submenuIPSummary
        elif name == "EBPPReconciliation":
            submenu = self.submenuEBPPReconciliation
        elif name == "ClientIDSummary":
            submenu = self.submenuClientIDSummary
        elif name == "CashSummary":
            submenu = self.submenuCashSummary
        elif name == "DepartmentSummary":
            submenu = self.submenuDepartmentSummary
        elif name == "DonationsSummary":
            submenu = self.submenuDonationsSummary
        else:
            submenu = " "
            print("Submenu not found")

        error += self.help.click_button(self.page, submenu)

        if len(error) == 0:
            self.help.info_log(self.page, name + "is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill