from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class TokenSummaryPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Token Summary Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Reports', 'tokenSummary')
        try:
            self.txtFilterBy = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elements['txtFilterBy']['css'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickTextFilterBy(self):
        error = list()
        fill = dict()
        method = "Token Summary"
        error += self.help.click_button(self.page, self.txtFilterBy)

        if len(error) == 0:
            self.help.info_log(self.page, "The TextBox FilterBy is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill