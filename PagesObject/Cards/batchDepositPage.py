from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class batchDepositPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Batch Deposit Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Cards', 'batchDeposit')
        try:
            self.btnYes = self.wait.until(ec.visibility_of_element_located((By.ID, elements['btnYes']['css'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnNo = self.wait.until(ec.visibility_of_element_located((By.ID, "closeQuestion")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickBtnYes(self):
        error = list()
        fill = dict()
        method = "Batch Deposit"
        error += self.help.click_button(self.page, self.btnYes)

        if len(error) == 0:
            self.help.info_log(self.page, "The Btn Yes is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnNo(self):
        error = list()
        fill = dict()
        method = "Batch Deposit"
        error += self.help.click_button(self.page, self.btnNo)

        if len(error) == 0:
            self.help.info_log(self.page, "The Btn No is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill