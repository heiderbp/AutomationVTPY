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

        try:
            self.txtAbaNumber = self.wait.until(ec.visibility_of_element_located((By.ID, "abaNumber")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickTxtAbaNumber(self):
        error = list()
        fill = dict()
        method = "Use Token"
        error += self.help.click_button(self.page, self.txtAbaNumber)

        if len(error) == 0:
            self.help.info_log(self.page, "The Text Box Aba Number is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill