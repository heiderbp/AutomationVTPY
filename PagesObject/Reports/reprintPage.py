from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class ReprintPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Reprint Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Reports', 'reprint')
        try:
            self.cmbDataSeries = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elements['cmbDataSeries']['css'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnSubmit = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#app>div.v-application--wrap>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div.row.no-gutters>div.col-sm-12.col-lg-7.col-12>div:nth-child(2)>div.col-sm-6.col-lg-2.col-12>button")))
        except Exception as e:
            error_name = "Could not get the Search Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtSearch = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#transactionDetails>div.top-table.no-print>div>div:nth-child(1)>div>div>div>div.v-text-field__slot>input[type=text]")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickCmbDataSeries(self):
        error = list()
        fill = dict()
        method = "Reprint"
        error += self.help.click_button(self.page, self.cmbDataSeries)

        if len(error) == 0:
            self.help.info_log(self.page, "The ComboBox DataSeries is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnSubmit(self):
        error = list()
        fill = dict()
        method = "Submit"
        error += self.help.click_button(self.page, self.btnSubmit)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Submit is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnOpenSendEmail(self):
        error = list()
        fill = dict()
        method = "Open Send Email"

        try:
            self.btnOpenSendEmail = self.wait.until(ec.visibility_of_element_located((By.ID,"#openSendEmail")))
        except Exception as e:
            error_name = "Could not get the Open Send Email Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnOpenSendEmail)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Open Send Email is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeEmailTo(self, email):
        error = list()
        fill = dict()
        method = "Email To"

        try:
            self.txtEmail = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#emailTo")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.write_field_text(self.page, "Email To", self.txtEmail, email)

        if len(error) == 0:
            self.help.info_log(self.page, "Text Email is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtSearch(self, idTrx):
        error = list()
        fill = dict()
        method = "Reprint"

        error += self.help.write_field_text(self.page, "Search", self.txtSearch, idTrx)

        if len(error) == 0:
            self.help.info_log(self.page, "Text Search is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnDisplayReceipt(self):
        error = list()
        fill = dict()
        method = "Display Receipt"

        try:
            self.btnDisplayReceipt = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#transactionDetails>div.v-data-table__wrapper>table>tbody>tr:nth-child(1)>td.text-xs-center.no-print>button")))
        except Exception as e:
            error_name = "Could not get the Search Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnDisplayReceipt)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Display Receipt is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

