import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class ManageTokenPage:
    def __init__(self, driver, helps, card):
        self.driver = driver
        self.help = helps
        self.page = "Manage Token Page"
        self.cardType = card
        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Cards', 'manageToken')

        try:
            self.txtLastFourDigits = self.wait.until(ec.visibility_of_element_located((By.ID, elements['txtLastFourDigits']['css'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbNewCardToken = self.wait.until(ec.visibility_of_element_located((By.ID, "newCardToken")))
        except Exception as e:
            error_name = "Could not get the New Card Token button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

    def clickTxtLastFourDigits(self):
        error = list()
        fill = dict()
        method = "Manage Token"
        error += self.help.click_button(self.page, self.txtLastFourDigits)

        if len(error) == 0:
            self.help.info_log(self.page, "The Text Last Four Digits is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnNewCardToken(self):
        error = list()
        fill = dict()
        method = "Manage Token New Card Token"
        error += self.help.click_button(self.page, self.cmbNewCardToken)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button New Card Token is clicked correctly")

            try:
                self.txtCustomerCode = self.wait.until(ec.visibility_of_element_located((By.ID, "customerCode")))
            except Exception as e:
                error_name = "Could not get the Customer Code input text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtCardNumber = self.wait.until(ec.visibility_of_element_located((By.ID, "cardNumber")))
            except Exception as e:
                error_name = "Could not get the Card Number text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtMonth = self.wait.until(ec.visibility_of_element_located((By.ID, "month")))
            except Exception as e:
                error_name = "Could not get the Month text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtYear = self.wait.until(ec.visibility_of_element_located((By.ID, "year")))
            except Exception as e:
                error_name = "Could not get the Year text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtNameOnCard = self.wait.until(ec.visibility_of_element_located((By.ID, "nameOnCard")))
            except Exception as e:
                error_name = "Could not get the Name On Card text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtToken = self.wait.until(ec.visibility_of_element_located((By.ID, "token")))
            except Exception as e:
                error_name = "Could not get the Token text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtEmail = self.wait.until(ec.visibility_of_element_located((By.ID, "email")))
            except Exception as e:
                error_name = "Could not get the Email text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtAddress = self.wait.until(ec.visibility_of_element_located((By.ID, "address")))
            except Exception as e:
                error_name = "Could not get the Address text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtZipCode = self.wait.until(ec.visibility_of_element_located((By.ID, "zipCode")))
            except Exception as e:
                error_name = "Could not get the Customer Code input text item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.btnSbmt = self.wait.until(ec.visibility_of_element_located((By.ID, "btn-sbmt")))
            except Exception as e:
                error_name = "Could not get the button submit: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def fillform(self):
        error = list()
        fill = dict()

        self.cards = self.help.get_card()
        self.card = self.cards['cards'][self.cardType]

        method = "Manage Token"

        data = self.help.generate_info()

        self.month = data["month"]
        self.year = data["year"]
        self.nameOnCard = data["name"]
        self.invoice = data["invoice"]
        self.email = data["email"]
        self.address = self.cards["additional"]["avs"]
        self.zip = self.cards["additional"]["zip"]

        if self.cardType.lower() == "amex":
            self.cvv = self.cards['cvv'][self.cardType]
        else:
            self.cvv = self.cards['cvv']['others']

        error += self.help.write_field_text(self.page, "Customer Code", self.txtCustomerCode, "75841")
        error += self.help.write_field_text(self.page, "Card Number", self.txtCardNumber, self.card)
        error += self.help.write_field_text(self.page, "month", self.txtMonth, self.month)
        error += self.help.write_field_text(self.page, "year", self.txtYear, self.year)
        error += self.help.write_field_text(self.page, "nameOnCard", self.txtNameOnCard, self.nameOnCard)
        error += self.help.write_field_text(self.page, "token", self.txtToken, "")
        try:
            self.txtCvv = self.wait.until(ec.visibility_of_element_located((By.ID, "cvv")))
            self.txtCvvExist = 1
        except Exception as e:
            self.txtCvvExist = 0
            error_name = "Could not get the Cvv text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if self.txtCvvExist == 1:
            error += self.help.write_field_text(self.page, "cvv", self.txtCvv, self.cvv)

        error += self.help.write_field_text(self.page, "email", self.txtEmail, self.email)
        error += self.help.write_field_text(self.page, "address", self.txtAddress, self.address)
        error += self.help.write_field_text(self.page, "zipCode", self.txtZipCode, self.zip)

        if self.btnSbmt.get_attribute("disabled"):
            self.help.info_log(self.page, "The Button Submit is disabled")
        else:
            error += self.help.click_button(self.page, self.btnSbmt)

            if len(error) == 0:
                self.help.info_log(self.page, "Button Submit is clicked correctly")

                try:
                    self.btnSubmitConfirmAlert = self.wait.until(ec.visibility_of_element_located((By.ID, "submitConfirmAlert")))
                except Exception as e:
                    error_name = "Could not get the Button Submit Confirm Alert: {}".format(str(e))
                    self.help.error_log(self.page, error_name)
                    error.append(error_name)

                error += self.help.click_button(self.page, self.btnSubmitConfirmAlert)
            else:
                fill = self.help.make_error_list(self.driver, method, error)


        if len(error) == 0:
            self.help.info_log(self.page, "The fill form correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def fillformCloneData(self):
        error = list()
        fill = dict()

        self.cards = self.help.get_card()
        self.card = self.cards['cards'][self.cardType]

        method = "Manage Token"

        error += self.help.write_field_text(self.page, "Customer Code", self.txtCustomerCode, "75841")
        error += self.help.write_field_text(self.page, "Card Number", self.txtCardNumber, self.card)
        error += self.help.write_field_text(self.page, "month", self.txtMonth, self.month)
        error += self.help.write_field_text(self.page, "year", self.txtYear, self.year)
        error += self.help.write_field_text(self.page, "nameOnCard", self.txtNameOnCard, self.nameOnCard)
        error += self.help.write_field_text(self.page, "token", self.txtToken, "")

        try:
            self.txtCvv = self.wait.until(ec.visibility_of_element_located((By.ID, "cvv")))
            self.txtCvvExist = 1
        except Exception as e:
            self.txtCvvExist = 0
            error_name = "Could not get the Cvv text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if self.txtCvvExist == 1:
            error += self.help.write_field_text(self.page, "cvv", self.txtCvv, self.cvv)

        error += self.help.write_field_text(self.page, "email", self.txtEmail, self.email)
        error += self.help.write_field_text(self.page, "address", self.txtAddress, self.address)
        error += self.help.write_field_text(self.page, "zipCode", self.txtZipCode, self.zip)

        if self.btnSbmt.get_attribute("disabled"):
            self.help.info_log(self.page, "The Button Submit is disabled")
        else:
            error += self.help.click_button(self.page, self.btnSbmt)

            if len(error) == 0:
                self.help.info_log(self.page, "Button Submit is clicked correctly")

                try:
                    self.btnSubmitConfirmAlert = self.wait.until(ec.visibility_of_element_located((By.ID, "submitConfirmAlert")))
                except Exception as e:
                    error_name = "Could not get the Button Submit Confirm Alert: {}".format(str(e))
                    self.help.error_log(self.page, error_name)
                    error.append(error_name)

                error += self.help.click_button(self.page, self.btnSubmitConfirmAlert)
            else:
                fill = self.help.make_error_list(self.driver, method, error)


        if len(error) == 0:
            self.help.info_log(self.page, "The fill form correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def getTextFromMessage(self):
        error = list()
        fill = dict()
        method = "Get Text From Message"

        try:
            self.txtToken = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-dialog__content.v-dialog__content--active>div>div>div.v-card__text")))
            self.token = self.txtToken.text[self.txtToken.text.index("ID: ")+4:self.txtToken.text.index("ID: ")+12]
            print("El token es: " + self.token)
        except Exception as e:
            error_name = "Could not get the text Token: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnOkMessage = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#app>div.v-dialog__content.v-dialog__content--active>div>div>div.v-card__actions>button:nth-child(4)")))
        except Exception as e:
            error_name = "Could not get the Button OK from Message: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if len(error) == 0:
            self.help.info_log(self.page, "get text correctly")

            error += self.help.click_button(self.page, self.btnOkMessage)

            if len(error) == 0:
                self.help.info_log(self.page, "The Button ok is clicked correctly")
            else:
                self.help.make_error_list(self.driver, method, error)
        else:
            self.help.info_log(self.page, "The fill form is not correct Page:"+method)

        return self.token

    def actionsClickTxtLastFourDigits(self):
        self.clickTxtLastFourDigits()


    def createNewCardToken(self):
        self.clickBtnNewCardToken()

    def getToken(self):
        return self.getTextFromMessage()