import time

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
        error = list()
        self.error = dict()

        try:
            self.username = self.wait.until(ec.visibility_of_element_located((By.ID,'userName')))
        except Exception as e:
            error_name = "Could not get the userName textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.password = self.wait.until(ec.visibility_of_element_located((By.ID,'password')))
        except Exception as e:
            error_name = "Could not get the password textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.merchant = self.wait.until(ec.visibility_of_element_located((By.ID,'merchant')))
        except Exception as e:
            error_name = "Could not get the merchant textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.submitLogin = self.wait.until(ec.visibility_of_element_located((By.ID,'submitLogin')))
        except Exception as e:
            error_name = "Could not get the submitLogin textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.resetPassword = self.wait.until(ec.visibility_of_element_located((By.ID,'resetPassword')))
        except Exception as e:
            error_name = "Could not get the Reset Password link: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)



    def fillFrom(self, username, password, merchant):
        error = list()
        fill = dict()
        method = "Login Form"

        error += self.help.write_field_text(self.page, "userName",  self.username, username)
        error += self.help.write_field_text(self.page, "password", self.password, password)
        error += self.help.write_field_text(self.page, "merchant", self.merchant, merchant)
        
        print(username, password, merchant)
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

    def clicksubmitLoginNewPassword(self, new_password, repeat_new_password):
        error = list()
        fill = dict()
        method = "Button Login New password"
        error += self.help.click_button(self.page, self.submitLogin)

        try:
            self.new_password = self.wait.until(ec.visibility_of_element_located((By.ID,'newPassword')))
        except Exception as e:
            error_name = "Could not get the password textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.repeatNewPassword = self.wait.until(ec.visibility_of_element_located((By.ID,'repeatNewPassword')))
        except Exception as e:
            error_name = "Could not get the repeat New Password textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.changePassword = self.wait.until(ec.visibility_of_element_located((By.ID,'changePassword')))
        except Exception as e:
            error_name = "Could not get the repeat New Password textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        time.sleep(2)

        error += self.help.write_field_text(self.page, "new_password",  self.new_password, new_password)
        error += self.help.write_field_text(self.page, "repeatNewPassword", self.repeatNewPassword, repeat_new_password)

        error += self.help.click_button(self.page, self.changePassword)

        if len(error) == 0:
            self.help.info_log(self.page, "login New Password was clicked")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clicksubmitLoginNewPasswordCancel(self):
        error = list()
        fill = dict()
        method = "Button Login New password"
        error += self.help.click_button(self.page, self.submitLogin)

        try:
            self.cancel = self.wait.until(ec.visibility_of_element_located((By.ID,'cancel')))
        except Exception as e:
            error_name = "Could not get the repeat New Password textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        time.sleep(2)

        error += self.help.click_button(self.page, self.cancel)

        if len(error) == 0:
            self.help.info_log(self.page, "login New Password was clicked")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill


    def clickResetPassword(self, userType):
        error = list()
        fill = dict()
        method = "Button Reset Password"
        error += self.help.click_button(self.page, self.resetPassword)
        mid = self.help.get_parameters()["mid"][userType]
        user = self.help.get_parameters()["users"][userType]

        if len(error) == 0:
            self.help.info_log(self.page, "Reset Password was clicked")

            try:
                self.title_modal_window = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#inspire>div.v-dialog__content.v-dialog__content--active>div>div>div.v-card__title')))
            except Exception as e:
                error_name = "Could not get the title from modal window: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            if self.title_modal_window.text == 'Restore Password':

                try:
                    self.modal_username = self.wait.until(ec.visibility_of_element_located((By.ID,'userRestore')))
                except Exception as e:
                    error_name = "Could not get the username text: {}".format(str(e))
                    self.help.error_log(self.page, error_name)
                    error.append(error_name)

                try:
                    self.modal_merchant = self.wait.until(ec.visibility_of_element_located((By.ID,'merchantRestore')))
                except Exception as e:
                    error_name = "Could not get the merchant text: {}".format(str(e))
                    self.help.error_log(self.page, error_name)
                    error.append(error_name)

                try:
                    self.modal_submit = self.wait.until(ec.visibility_of_element_located((By.ID,'submitRestorePassword')))
                except Exception as e:
                    error_name = "Could not get the submit button: {}".format(str(e))
                    self.help.error_log(self.page, error_name)
                    error.append(error_name)

                error += self.help.write_field_text(self.page, "userName", self.modal_username, user)
                error += self.help.write_field_text(self.page, "merchant", self.modal_merchant, mid)

                error += self.help.click_button(self.page, self.modal_submit)

                # print(username, password, merchant)
                if len(error) == 0:
                    self.help.info_log(self.page, "The user, password and merchant fields were complete")
                else:
                    fill = self.help.make_error_list(self.driver, method, error)

            else:
                error_name = "Could not get the title Restore Password from modal window"
                self.help.error_log(self.page, error_name)
                error.append(error_name)
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def actionsResetPassword(self,userType):
        self.clickResetPassword(userType)

    def actionsLogin(self, userType):
        mid = self.help.get_parameters()["mid"][userType]
        user = self.help.get_parameters()["users"][userType]
        password = self.help.get_parameters()["passwords"][userType]
        self.fillFrom(user, password, mid)
        self.clicksubmitLogin()

    def actionsLoginNewPasswordCancel(self, userType, pw):
        mid = self.help.get_parameters()["mid"][userType]
        user = self.help.get_parameters()["users"][userType]
        password = pw
        self.fillFrom(user, password, mid)
        self.clicksubmitLoginNewPasswordCancel()

    def actionsLoginNewPassword(self, userType, pw, new_pw, repeat_new_pw):
        mid = self.help.get_parameters()["mid"][userType]
        user = self.help.get_parameters()["users"][userType]
        password = pw
        self.fillFrom(user, password, mid)
        self.clicksubmitLoginNewPassword(new_pw,repeat_new_pw)
