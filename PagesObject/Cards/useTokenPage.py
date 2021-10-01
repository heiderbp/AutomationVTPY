from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class UseTokenPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Use Token Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Cards', 'useToken')

        try:
            self.txtLastFourDigits = self.wait.until(ec.visibility_of_element_located((By.ID, elements['txtLastFourDigits']['id'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtEmail = self.wait.until(ec.visibility_of_element_located((By.ID, "email")))
        except Exception as e:
            error_name = "Could not get the Email input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtClientId = self.wait.until(ec.visibility_of_element_located((By.ID, "clientId")))
        except Exception as e:
            error_name = "Could not get the Email input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtFilter = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#customTab>div>div>div:nth-child(3)>div:nth-child(1)>div>div>div.v-input__slot>div.v-text-field__slot>input[type=text]")))
        except Exception as e:
            error_name = "Could not get the Filter input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnSearchCardTokens = self.wait.until(ec.visibility_of_element_located((By.ID, "searchCardTokens")))
        except Exception as e:
            error_name = "Could not get the Search card Token Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickTxtLastFourDigits(self):
        error = list()
        fill = dict()
        method = "Use Token"
        error += self.help.click_button(self.page, self.txtLastFourDigits)

        if len(error) == 0:
            self.help.info_log(self.page, "The Text box Last Four Digits is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnSearchCardTokens(self):
        error = list()
        fill = dict()
        method = "Use Token"
        error += self.help.click_button(self.page, self.btnSearchCardTokens)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Search Card Tokens is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnUseCardToken(self):
        error = list()
        fill = dict()
        method = "Use Token Button Use Card Token"

        try:
            self.btnCardToken = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#cardTokens>div.v-data-table__wrapper>table>tbody>tr:nth-child(1)>td.text-center.no-print>nobr>button:nth-child(8)")))
        except Exception as e:
            error_name = "Could not get the card Token Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnCardToken)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Card Tokens is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill


    def writeTxtEmail(self, text):
        error = list()
        fill = dict()
        method = "Role Search"

        error += self.help.write_field_text(self.page, "Search Text", self.txtEmail, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The Email textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtClientId(self, text):
        error = list()
        fill = dict()
        method = "Client Id Search"

        error += self.help.write_field_text(self.page, "Search Client Id ", self.txtClientId, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtFilter(self, text):
        error = list()
        fill = dict()
        method = "Text Search"

        error += self.help.write_field_text(self.page, "Search Text Filter", self.txtFilter, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def actionsClickCmbMerchant(self):
        self.clickTxtLastFourDigits()

    def actionsUseToken(self, token):
        self.writeTxtEmail("%")
        self.writeTxtClientId("%")
        self.writeTxtFilter(token)
        self.clickBtnSearchCardTokens()
        self.clickBtnUseCardToken()
