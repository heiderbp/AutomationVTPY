from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class EmailPage:


    def __init__(self, driver, helps):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.help = helps
        self.page = "Email Page"
        error = list()
        self.error = dict()

        try:
            self.username = self.wait.until(ec.visibility_of_element_located((By.ID,'addOverlay')))
        except Exception as e:
            error_name = "Could not get the userName textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.button_go = self.wait.until(ec.visibility_of_element_located((By.ID,'go-to-public')))
        except Exception as e:
            error_name = "Could not get the go button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def click_first_element(self):
        error = list()
        fill = dict()
        method = "Button Go"

        try:
            self.first_list_element = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#inbox_pane>div.wrapper-primary-table.scrollbar>div>div.os-padding>div>div>table>tbody>tr:nth-child(1)>td:nth-child(2)')))
        except Exception as e:
            error_name = "Could not get the element list: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.first_list_element)

        if len(error) == 0:
            self.help.info_log(self.page, "first_list_element was clicked")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def get_password_from_email(self):
        error = list()
        method = "Html msg body"

        try:
            self.html_msg_body = self.wait.until(ec.visibility_of_element_located((By.ID, 'html_msg_body')))
        except Exception as e:
            error_name = "Could not get the element list: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        self.driver.switch_to.frame(self.html_msg_body);

        try:
            self.text_html_msg_body = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'body>table>tbody>tr:nth-child(3)>td>p:nth-child(1)')))
        except Exception as e:
            error_name = "Could not get the element list: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if len(error) == 0:
            self.help.info_log(self.page, "Get Msg from Email is ok")
        else:
            self.help.make_error_list(self.driver, method, error)

        return self.text_html_msg_body.text[-8:]

    def click_go(self):
        error = list()
        fill = dict()
        method = "Button Go"
        error += self.help.click_button(self.page, self.button_go)

        if len(error) == 0:
            self.help.info_log(self.page, "go was clicked")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def write_user(self, user):
        error = list()
        fill = dict()
        method = "inbox text"

        error += self.help.write_field_text(self.page, "addOverlay", self.username, self.help.get_parameters()["email"][user])

        if len(error) == 0:
            self.help.info_log(self.page, "The user for inbox is complete")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill