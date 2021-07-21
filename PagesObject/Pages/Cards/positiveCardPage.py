from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class PositiveCardVerificationPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Positive Card Verification Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.txtCustomerCode = self.wait.until(ec.visibility_of_element_located((By.ID, "customerCode")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickTxtCustomerCode(self):
        error = list()
        fill = dict()
        method = "Positive Card Verification"
        error += self.help.click_button(self.page, self.txtCustomerCode)

        if len(error) == 0:
            self.help.info_log(self.page, "The Text Customer Code is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill