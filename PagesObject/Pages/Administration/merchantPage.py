from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MerchantPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Merchant Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Administration', 'merchant')
        try:
            self.tabMerchantData = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elements['tabMerchantData']['css'])))
        except Exception as e:
            error_name = "Could not get the Merchant Data tab item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.tabProcessingData = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div>div.v-card__text>form>div>div.v-item-group.theme--light.v-slide-group.v-tabs-bar.v-tabs-bar--show-arrows.primary--text>div.v-slide-group__wrapper>div>div:nth-child(3)")))
        except Exception as e:
            error_name = "Could not get the Processing Data tab item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.tabAdditionalData = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div>div.v-card__text>form>div>div.v-item-group.theme--light.v-slide-group.v-tabs-bar.v-tabs-bar--show-arrows.primary--text>div.v-slide-group__wrapper>div>div:nth-child(4)")))
        except Exception as e:
            error_name = "Could not get the Additional Data tab item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.merchantSave = self.wait.until(ec.visibility_of_element_located((By.ID, "save")))
        except Exception as e:
            error_name = "Could not get the merchant save button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if len(error) == 0:
            self.help.info_log(self.page, "Get Elements is ok")

    def clickTabMerchantData(self):
        error = list()
        fill = dict()
        method = "Merchant tab Merchant Data"

        try:
            self.txtName = self.wait.until(ec.visibility_of_element_located((By.ID, "name")))
        except Exception as e:
            error_name = "Could not get the Name Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtContactFirstName = self.wait.until(ec.visibility_of_element_located((By.ID, "contactFirstName")))
        except Exception as e:
            error_name = "Could not get the contact First Name Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtContactLastName = self.wait.until(ec.visibility_of_element_located((By.ID, "contactLastName")))
        except Exception as e:
            error_name = "Could not get the contact Last Name Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtContactEmail = self.wait.until(ec.visibility_of_element_located((By.ID, "contactEmail")))
        except Exception as e:
            error_name = "Could not get the contact Email Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtAddress1 = self.wait.until(ec.visibility_of_element_located((By.ID, "address1")))
        except Exception as e:
            error_name = "Could not get the address1 Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtAddress2 = self.wait.until(ec.visibility_of_element_located((By.ID, "address2")))
        except Exception as e:
            error_name = "Could not get the address2 Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtCity = self.wait.until(ec.visibility_of_element_located((By.ID, "city")))
        except Exception as e:
            error_name = "Could not get the City Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtZip = self.wait.until(ec.visibility_of_element_located((By.ID, "zip")))
        except Exception as e:
            error_name = "Could not get the Zip Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtDefaultTax = self.wait.until(ec.visibility_of_element_located((By.ID, "defaultTax")))
        except Exception as e:
            error_name = "Could not get the default Tax Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtSessionTimeout = self.wait.until(ec.visibility_of_element_located((By.ID, "sessionTimeout")))
        except Exception as e:
            error_name = "Could not get the session timeout Text Box item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)


        if self.tabMerchantData.get_attribute("aria-selected") == "false":
            error += self.help.click_button(self.page, self.tabMerchantData)

            if len(error) == 0:
                self.help.info_log(self.page, "Merchant Data tab clicked correctly")
            else:
                fill = self.help.make_error_list(self.driver, method, error)
        else:
            self.help.info_log(self.page, "The Merchant Data tab is already selected")

        return fill

    def clickTabProcessingData(self):
        error = list()
        fill = dict()
        method = "Merchant tab Processing Data"

     #   if self.tabProcessingData.get_attribute("aria-selected") == "false":
        error += self.help.click_button(self.page, self.tabProcessingData)

        if len(error) == 0:
            self.help.info_log(self.page, "Processing Data tab clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)
     #   else:
     #       self.help.info_log(self.page, "The Processing Data tab is already selected")

        return fill


    def clickTabAdditionalData(self):
        error = list()
        fill = dict()
        method = "Merchant Tab Additional Data"

        if self.tabAdditionalData.get_attribute("aria-selected") == "false":
            error += self.help.click_button(self.page, self.tabAdditionalData)

            if len(error) == 0:
                self.help.info_log(self.page, "Additional Data tab clicked correctly")
            else:
                fill = self.help.make_error_list(self.driver, method, error)
        else:
            self.help.info_log(self.page, "The Additional Data tab is already selected")

        return fill

    def clickmerchantsave(self):
        error = list()
        fill = dict()
        method = "Merchant Button Save"
        error += self.help.click_button(self.page, self.merchantSave)

        if len(error) == 0:
            self.help.info_log(self.page, "The save button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill