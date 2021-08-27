import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class UsersPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Users Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Administration', 'users')
        try:
            self.txtSearch = self.wait.until(ec.visibility_of_element_located((By.ID, elements['txtSearch']['id'])))
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
            self.txtResultUser = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                   "#tableUsers>div.v-data-table__wrapper>table>tbody>tr>td")))  # "#tableUsers>div>table>tbody>tr>td")))
        except Exception as e:
            error_name = "Could not get the ResultUser text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickUsersSearch(self):
        error = list()
        fill = dict()
        method = "User Search"
        error += self.help.click_button(self.page, self.txtSearch)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeUserSearch(self, text):
        error = list()
        fill = dict()
        method = "User Search"

        error += self.help.write_field_text(self.page, "Search Text Role", self.txtSearch, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def getTxtResultUser(self):
        error = list()
        fill = dict()
        method = "Role Result"
        text = str()
        text = self.help.get_text(self.page, self.txtResultUser)

        try:
            self.txtResultFirstRow = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableRoles>div>table>tbody>tr:nth-child(1)>td.text-xs-center.no-print")))

        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        return text

    def clickRowSelect(self):
        error = list()
        fill = dict()
        method = "New User"

        error += self.help.click_button(self.page, self.txtRowSelect)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is clicked correctly")

        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def fillform(self, text):
        error = list()
        fill = dict()
        method = "New User"

        try:
            self.txtUserId = self.wait.until(ec.visibility_of_element_located((By.ID, "userId")))
            self.txtUserId.send_keys(text)
        except Exception as e:
            error_name = "Could not get the userId input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtPassword = self.wait.until(ec.visibility_of_element_located((By.ID, "password")))
            self.txtPassword.send_keys("Cenpos@2")
        except Exception as e:
            error_name = "Could not get the password input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtRepeatPassword = self.wait.until(ec.visibility_of_element_located((By.ID, "repeatPassword")))
            self.txtRepeatPassword.send_keys("Cenpos@2")
        except Exception as e:
            error_name = "Could not get the repeatPassword input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtName = self.wait.until(ec.visibility_of_element_located((By.ID, "name")))
            self.txtName.send_keys("Andrea Bastidas")
        except Exception as e:
            error_name = "Could not get the name input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtDepartment = self.wait.until(ec.visibility_of_element_located((By.ID, "department")))
            self.txtDepartment.send_keys("QA")
        except Exception as e:
            error_name = "Could not get the department input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtEmail = self.wait.until(ec.visibility_of_element_located((By.ID, "email")))
            self.txtEmail.send_keys("heiderbp@hotmail.com")
        except Exception as e:
            error_name = "Could not get the email input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtCellPhoneNumber = self.wait.until(ec.visibility_of_element_located((By.ID, "cellPhoneNumber")))
            self.txtCellPhoneNumber.send_keys("323232323232")
        except Exception as e:
            error_name = "Could not get the cellPhoneNumber input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
         #   self.cmbInvoice = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div.v-card.v-sheet.theme--light>div.v-card__text>form>div>div:nth-child(1)>div>div:nth-child(8)>div>div>div.v-input__slot")))
         #   self.cmbInvoice.click()

            self.cmbInvoiceItem = self.wait.until(ec.visibility_of_element_located((By.ID, "invoiceOption")))

            self.cmbInvoiceItem.send_keys("Do Not")
            self.cmbInvoiceItem.send_keys(Keys.ENTER)

        except Exception as e:
            error_name = "Could not get the Invoice Combo box: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
        #    self.cmbRole = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div.v-card.v-sheet.theme--light>div.v-card__text>form>div>div:nth-child(1)>div>div:nth-child(9)>div>div>div.v-input__slot")))

         #   self.cmbRole.click()

            self.cmbRoleItems = self.wait.until(ec.visibility_of_element_located((By.ID, "hierarchyRoleId")))
            self.cmbRoleItems.send_keys("CenPOS Admin")
            self.cmbRoleItems.send_keys(Keys.ENTER)

        except Exception as e:
            error_name = "Could not get the Role Combo box: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbPrinterOption = self.wait.until(ec.visibility_of_element_located((By.ID, "receiptType")))
         #   self.cmbPrinterOption.click()
            self.cmbPrinterOption.send_keys("Receipts")
            self.cmbPrinterOption.send_keys(Keys.ENTER)
        except Exception as e:
            error_name = "Could not get the Printer Option Combo box: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.parametersSave = self.wait.until(ec.visibility_of_element_located((By.ID, "save")))
        except Exception as e:
            error_name = "Could not get the parameter save button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if len(error) == 0:
            self.help.info_log(self.page, "Get Elements is ok")

        return fill

    def clicksave(self):
        error = list()
        fill = dict()
        method = "Roles Page Button Save"
        error += self.help.click_button(self.page, self.parametersSave)

        if len(error) == 0:
            self.help.info_log(self.page, "The save button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill