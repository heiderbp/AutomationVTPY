from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.Locators import Locators


class administrationPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Administration Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.submenuRoles = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "1").replace("MENU", "2"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Roles: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuUser = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, "#app>div>nav>div.v-navigation-drawer__content>div>div:nth-child(2)>div>div.v-list-group__items>a:nth-child(2)")))
        except Exception as e:
            error_name = "Could not get the Administration menu item User: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuMerchant = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "3").replace("MENU", "2"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item Merchant: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuMerchantParameters = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "4").replace("MENU", "2"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item MerchantParameters: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuAccessControlList = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "5").replace("MENU", "2"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item AccessControlList: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuCountriesAcl = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "6").replace("MENU", "2"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item CountriesAcl: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submenuInvoiceTemplates = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.subMenu.replace("SUBMENU", "7").replace("MENU", "2"))))
        except Exception as e:
            error_name = "Could not get the Administration menu item InvoiceTemplates: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickSubmenu(self, name):
        error = list()
        fill = dict()
        method = "Submenu Boton" + name

        if name == "Roles":
            submenu = self.submenuRoles
        elif name == "Users":
            submenu = self.submenuUser
        elif name == "Merchant":
            submenu = self.submenuMerchant
        elif name == "MerchantParameters":
            submenu = self.submenuMerchantParameters
        elif name == "AccessControlList":
            submenu = self.submenuAccessControlList
        elif name == "CountriesAcl":
            submenu = self.submenuCountriesAcl
        elif name == "InvoiceTemplates":
            submenu = self.submenuInvoiceTemplates
        else:
            submenu = self.submenuRoles

        error += self.help.click_button(self.page, submenu)

        if len(error) == 0:
            self.help.info_log(self.page, "Successfully clicked on " + name)
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill
