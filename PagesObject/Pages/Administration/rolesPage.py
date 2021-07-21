from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class RolesPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Roles Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.txtSearch = self.wait.until(ec.visibility_of_element_located((By.ID, "search")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtRowSelect = self.wait.until(ec.visibility_of_element_located((By.ID, "rowSelect")))
        except Exception as e:
            error_name = "Could not get the Row Select Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtRolName = self.wait.until(ec.visibility_of_element_located((By.ID, "rolName")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbRol = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#app>div>main>div>div>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div>div>div:nth-of-type(2)>div")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbRolSelect = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#list-item-1564-0>div>div")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbBillingAddress = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#list-item-868-0>div")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtBillingAddressAmountTrigger = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input#input-689")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.chkBillingAddressSendEmailAlert = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input#input-689")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbZipCode = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#list-item-868-0>div")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickRoleSearch(self):
        error = list()
        fill = dict()
        method = "Role Search"
        error += self.help.click_button(self.page, self.txtSearch)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

