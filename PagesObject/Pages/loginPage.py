from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.help = helps
        self.page = "Login Page"

        self.username = self.wait.until(ec.visibility_of_element_located((By.ID,'userName')))
        self.password = self.wait.until(ec.visibility_of_element_located((By.ID,'password')))
        self.merchant = self.wait.until(ec.visibility_of_element_located((By.ID,'merchant')))
        self.submitLogin = self.wait.until(ec.visibility_of_element_located((By.ID,'submitLogin')))

    def fillFrom(self, username, password, merchant):
        error = list()
        fill = dict()
        method = "Login Form"

        error += self.help.write_field_text(self.page, "userName",  self.username, username)
        error += self.help.write_field_text(self.page, "password", self.password, password)
        error += self.help.write_field_text(self.page, "merchant", self.merchant, merchant)
        
        #print(username, password, merchant)
        if len(error) == 0:
            self.help.info_log(self.page, "The user, password and merchant fields were complete")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill


    def clicksubmitLogin(self):
        error = list()
        fill = dict()
        method = "Button Login"
        error += self.help.click_button(self.page, self.submitLogin)

        if len(error) == 0:
            self.help.info_log(self.page, "login was clicked")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill



