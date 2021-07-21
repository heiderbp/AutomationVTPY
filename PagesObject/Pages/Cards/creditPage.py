from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class CreditPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Credit Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)

        try:
            self.cmbMerchant = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div>div>div.col-lg-5.col-12>div>div.v-card__text.custom>div.cardForm>div>div:nth-child(3)>div.col-lg-8.col-12>div>div>div.v-input__slot")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickCmbMerchant(self):
        error = list()
        fill = dict()
        method = "Auth"
        error += self.help.click_button(self.page, self.cmbMerchant)

        if len(error) == 0:
            self.help.info_log(self.page, "The Combo box Merchant is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill