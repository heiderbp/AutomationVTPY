from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class UsersPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Users Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Administration', 'users')
        try:
            self.txtSearch = self.wait.until(ec.visibility_of_element_located((By.ID, elements['txtSearch']['id'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtRowSelect = self.wait.until(ec.visibility_of_element_located((By.ID, "rowSelect")))
        except Exception as e:
            error_name = "Could not get the Row Select Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickUsersSearch(self):
        error = list()
        fill = dict()
        method = "User Search"
        error += self.help.click_button(self.page, self.txtSearch)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

