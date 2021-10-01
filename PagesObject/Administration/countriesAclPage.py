from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class CountriesACLPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Countries ACL Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Administration', 'countriesAcl')
        try:
            self.chkAllowedCountries = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elements['chkAllowedCountries']['css'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickChkAllowedCountries(self):
        error = list()
        fill = dict()
        method = "Countries ACL"
        error += self.help.click_button(self.page, self.chkAllowedCountries)

        if len(error) == 0:
            self.help.info_log(self.page, "The Allowed Countries checkbox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill