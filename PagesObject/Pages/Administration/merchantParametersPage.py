from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import random


class MerchantParametersPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Merchant Parameters Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Administration', 'merchantParameters')

        try:
            self.parametersAvs = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elements['tabParametersAvs']['css'])))
        except Exception as e:
            error_name = "Could not get the parameter avs tab item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.parametersZip = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div>div>div.row.align-center.justify-center>div>div>div>div:nth-child(1)>div>div>div>div.v-item-group.theme--light.v-slide-group.v-tabs-bar.primary--text>div.v-slide-group__wrapper>div>div:nth-child(3)")))
        except Exception as e:
            error_name = "Could not get the parameter zip tab item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.parametersCvv = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div>div>div.row.align-center.justify-center>div>div>div>div:nth-child(1)>div>div>div>div.v-item-group.theme--light.v-slide-group.v-tabs-bar.primary--text>div.v-slide-group__wrapper>div>div:nth-child(4)")))
        except Exception as e:
            error_name = "Could not get the parameter cvv tab item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.parametersSave = self.wait.until(ec.visibility_of_element_located((By.ID, "save")))
        except Exception as e:
            error_name = "Could not get the parameter save button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if len(error) == 0:
            self.help.info_log(self.page, "Get Elements is ok")

    def clicktabavs(self):
        error = list()
        fill = dict()
        method = "Merchant Parameters tab AVS"

        if self.parametersAvs.get_attribute("aria-selected") == "false":
            error += self.help.click_button(self.page, self.parametersAvs)

            if len(error) == 0:
                self.help.info_log(self.page, "AVS tab clicked correctly")
            else:
                fill = self.help.make_error_list(self.driver, method, error)
        else:
            self.help.info_log(self.page, "The AVS tab is already selected")

        return fill

    def clicktabzip(self):
        error = list()
        fill = dict()
        method = "Merchant Parameters tab ZIP"

        if self.parametersZip.get_attribute("aria-selected") == "false":
            error += self.help.click_button(self.page, self.parametersZip)
            if len(error) == 0:
                self.help.info_log(self.page, "ZIP tab clicked correctly")
            else:
                fill = self.help.make_error_list(self.driver, method, error)
        else:
            self.help.info_log(self.page, "The ZIP tab is already selected")

        return fill

    def clicktabcvv(self):
        error = list()
        fill = dict()
        method = "Merchant Parameters tab CVV"

        if self.parametersCvv.get_attribute("aria-selected") == "false":
            error += self.help.click_button(self.page, self.parametersCvv)

            if len(error) == 0:
                self.help.info_log(self.page, "CVV tab clicked correctly")
            else:
                fill = self.help.make_error_list(self.driver, method, error)
        else:
            self.help.info_log(self.page, "The CVV tab is already selected")

        return fill

    def clickcheckavs(self):
        error = list()
        fill = dict()
        method = "Checkbox AVS"

        for a in range(1, 18):
            num = random.randrange(1, 3)
            if num == 1:
                parameterscheckavs = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div>div>div.row.align-center.justify-center>div>div>div>div:nth-child(1)>div>div>div>div.v-window.v-item-group.theme--light.v-tabs-items>div>div.v-window-item.v-window-item--active>div>div.v-card__text>div>div:nth-child(" + str(a) + ")>div>div>div.v-input__slot>div>div")))
                error += self.help.click_button(self.page, parameterscheckavs)
                if len(error) == 0:
                    self.help.info_log(self.page, "Checkbox (" + str(a) + ") is clicked correctly")
                else:
                    fill = self.help.make_error_list(self.driver, method, error)


        if len(error) == 0:
            self.help.info_log(self.page, "The checkbox tab AVS is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickcheckzip(self):
        error = list()
        fill = dict()
        method = "Checkbox Zip"

        for a in range(1, 19):
            num = random.randrange(1, 3)
            if num == 1:
                parameterscheckzip = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div>div>div.row.align-center.justify-center>div>div>div>div:nth-child(1)>div>div>div>div.v-window.v-item-group.theme--light.v-tabs-items>div>div.v-window-item.v-window-item--active>div>div.v-card__text>div>div:nth-child(" + str(a) + ")>div>div>div.v-input__slot>div>div")))
                error += self.help.click_button(self.page, parameterscheckzip)
                if len(error) == 0:
                    self.help.info_log(self.page, "Checkbox (" + str(a) + ") is clicked correctly")
                else:
                    fill = self.help.make_error_list(self.driver, method, error)

        if len(error) == 0:
            self.help.info_log(self.page, "The checkbox tab ZIP is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickcheckcvv(self):
        error = list()
        fill = dict()
        method = "Checkbox Cvv"

        for a in range(1, 12):
            num = random.randrange(1, 3)
            if num == 1:
                parameterscheckcvv = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div>div>div.row.align-center.justify-center>div>div>div>div:nth-child(1)>div>div>div>div.v-window.v-item-group.theme--light.v-tabs-items>div>div.v-window-item.v-window-item--active>div>div.v-card__text>div>div:nth-child(" + str(a) + ")>div>div>div.v-input__slot>div>div")))
                error += self.help.click_button(self.page, parameterscheckcvv)
                if len(error) == 0:
                    self.help.info_log(self.page, "Checkbox (" + str(a) + ") is clicked correctly")
                else:
                    fill = self.help.make_error_list(self.driver, method, error)

        if len(error) == 0:
            self.help.info_log(self.page, "The checkbox tab CVV is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clicksave(self):
        error = list()
        fill = dict()
        method = "Merchant Parameters Button Save"
        error += self.help.click_button(self.page, self.parametersSave)

        if len(error) == 0:
            self.help.info_log(self.page, "The save button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill
