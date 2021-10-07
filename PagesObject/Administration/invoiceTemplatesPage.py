from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class InvoiceTemplatesPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Invoice Templates Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Administration', 'invoiceTemplates')
        try:
            self.cmbSale = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elements['cmbSale']['css'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmb = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div>div>div.col-lg-6.col-12>div>div.v-card__text>div>div>table>tbody>tr:nth-child(1)>td:nth-child(2)>div>div>div")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnSave = self.wait.until(ec.visibility_of_element_located((By.ID, "save")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickCmbSale(self):
        error = list()
        fill = dict()
        method = "Invoice Templates"
        error += self.help.click_button(self.page, self.cmbSale)

        if len(error) == 0:
            self.help.info_log(self.page, "The Combo box Sale is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickCmb(self):
        error = list()
        fill = dict()
        method = "Invoice Templates"
        error += self.help.click_button(self.page, self.cmb)

        if len(error) == 0:
            self.help.info_log(self.page, "The ComboBox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeCmb(self, text):
        error = list()
        fill = dict()
        method = "Invoice Templates"

        try:
            self.cmbWrite = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div>div>div.col-lg-6.col-12>div>div.v-card__text>div>div>table>tbody>tr:nth-child(1)>td:nth-child(2)>div>div>div>div.v-select__slot>div.v-select__selections>input[type=text]")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.write_field_text(self.page, "Search Text Role", self.cmbWrite, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickCmbItem(self):
        error = list()
        fill = dict()
        method = "Invoice Templates"
        cmbItem = None

        try:
            cmbItem = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(1)")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, cmbItem)

        if len(error) == 0:
            self.help.info_log(self.page, "The Combo Item is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnSave(self):
        error = list()
        fill = dict()
        method = "Invoice Templates"
        error += self.help.click_button(self.page, self.btnSave)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Save is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def actionTemplateTransactionSetDefault(self):
        self.clickCmb()
        self.clickCmbItem()
        self.clickBtnSave()

    def actionTemplateTransactionSetCustom(self):
        self.clickCmb()
        self.clickCmbItem()
        self.writeCmb('custom')
        self.writeCmb(Keys.ENTER)
        self.clickBtnSave()