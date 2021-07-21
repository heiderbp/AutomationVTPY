from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class VoidPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Void Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.cmbDataSeries = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#customTab>div>div.v-card__text>div:nth-child(1)>div:nth-child(1)>div>div>div.v-input__slot")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickCmbDataSeries(self):
        error = list()
        fill = dict()
        method = "Void"
        error += self.help.click_button(self.page, self.cmbDataSeries)

        if len(error) == 0:
            self.help.info_log(self.page, "The Combo box Data Series is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill