from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class HeaderP:
    def __init__(self, driver, helps, flag=True):
        self.driver = driver
        self.help = helps

        self.page = "Header Page"

        error = list()
        self.error = dict()

        self.wait = WebDriverWait(self.driver, 5)

        self.btnProfile = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#app>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large')))

    def clickbtnProfile(self):
        error = list()
        fill = dict()
        method = "Header Button Profile"
        ##  error += self.btnProfile.click()
        error += self.help.click_button(self.page, self.btnProfile)
        if len(error) == 0:
            self.help.info_log(self.page, "Profile is clicked correctly")
            try:
                self.profileResetPassword = self.driver.find_element(By.CSS_SELECTOR,
                                                                     "body>div>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(1)")
            except Exception as e:
                error_name = "Could not get the Reset Password item from options Profile: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.profileMultiMerchant = self.driver.find_element(By.CSS_SELECTOR,
                                                                     "#app>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(2)")
            except Exception as e:
                error_name = "Could not get the Multi Merchant item from options Profile: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickProfileResetPassword(self):
        error = list()
        fill = dict()
        method = "Header Button Reset Password"

        error += self.help.click_button(self.page, self.profileResetPassword)
        if len(error) == 0:
            self.help.info_log(self.page, "Profile is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtOldPassword(self, userType):
        error = list()
        fill = dict()
        method = "Text Old Password"

        try:
            self.profileResetOldPassword = self.driver.find_element(By.ID, "password")
        except Exception as e:
            error_name = "Could not get the Old Password Textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.write_field_text(self.page, "Old Password", self.profileResetOldPassword,
                                            self.help.get_parameters()["users"][userType])

        if len(error) == 0:
            self.help.info_log(self.page, "The Old Password fields were complete")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtNewPassword(self, text):
        error = list()
        fill = dict()
        method = "Text New Password"

        try:
            self.profileResetNewPassword = self.driver.find_element(By.ID, "newPassword")
        except Exception as e:
            error_name = "Could not get the New Password Textbox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.write_field_text(self.page, "New Password", self.profileResetNewPassword, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The New Password fields were complete")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtConfirmPassword(self, text):
        error = list()
        fill = dict()
        method = "Text Confirm Password"

        try:
            self.profileResetConfirmPassword = self.driver.find_element(By.ID, "repeatPassword")
        except Exception as e:
            error_name = "Could not get the Repeat Password TextBox: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.write_field_text(self.page, "Confirm Password", self.profileResetConfirmPassword, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The Confirm Password fields were complete")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickProfileResetSubmit(self):
        error = list()
        fill = dict()
        method = "Header Button Submit"

        try:
            self.profileResetSubmit = self.driver.find_element(By.ID, "submitChangePassword")
        except Exception as e:
            error_name = "Could not get the Submit Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.profileResetSubmit)

        if len(error) == 0:
            self.help.info_log(self.page, "Submit is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickProfileMultiMerchant(self):
        error = list()
        fill = dict()
        method = "Header Button Multi Merchant"

        error += self.help.click_button(self.page, self.profileMultiMerchant)
        if len(error) == 0:
            self.help.info_log(self.page, "Profile MultiMerchant is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickMultiMerchantElement(self):
        error = list()
        fill = dict()
        method = "Header Multi Merchant Item"

        try:
            self.multiMerchantElement = self.driver.find_element(By.CSS_SELECTOR,
                                                                 "#app>div.v-dialog__content.v-dialog__content--active>div>div>div.v-card__text>div>div>div>div.v-data-table__wrapper>table>tbody>tr")
        except Exception as e:
            error_name = "Could not get the Multi Merchant Item from list: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        action = ActionChains(self.driver)

        action.double_click(self.multiMerchantElement).perform()

        return fill

    def clickbtnLogout(self):
        error = list()
        fill = dict()
        method = "Header Button Logout"
        self.btnLogout = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                           '#app>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(3)')))
        error += self.help.click_button(self.page, self.btnLogout)

        if len(error) == 0:
            self.help.info_log(self.page, "Logout is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def actionsSwitchMerchant(self):
        self.clickbtnProfile()
        self.clickProfileMultiMerchant()
        self.clickMultiMerchantElement()

    def actionsChangePasswordFromTopUser(self, new_password, confirm_password):
        self.clickbtnProfile()
        self.clickProfileResetPassword()
        self.writeTxtOldPassword('standard')
        self.writeTxtNewPassword(new_password)
        self.writeTxtConfirmPassword(confirm_password)
        self.clickProfileResetSubmit()

    def actionsSwitchMerchant(self):
        self.clickbtnProfile()
        self.clickProfileMultiMerchant()
        self.clickMultiMerchantElement()

    def actionsLogout(self):
        self.clickbtnProfile()
        self.clickbtnLogout()

