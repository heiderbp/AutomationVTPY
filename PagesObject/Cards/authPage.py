from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class AuthPage:
    def __init__(self, driver, helps, card=str()):
        self.driver = driver
        self.help = helps
        self.page = "Auth Page"

        self.cardType = card

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Cards', 'auth')

        try:
            self.cmbMerchant = self.wait.until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, elements['cmbMerchant']['css'])))
        except Exception as e:
            error_name = "Could not get the Combo box cmbMerchant: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtAmount = self.wait.until(ec.visibility_of_element_located((By.ID, "amount")))
        except Exception as e:
            error_name = "Could not get the Amount input text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtRadioMOTO = self.wait.until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, "#radioButtonTypes>div:nth-child(2)")))
        except Exception as e:
            error_name = "Could not get the MOTO Radio Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtRadioSale = self.wait.until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, "#radioButtonTypes>div:nth-child(1)")))
        except Exception as e:
            error_name = "Could not get the Sale Radio Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtCardNumber = self.wait.until(ec.visibility_of_element_located((By.ID, "cardNumber")))
        except Exception as e:
            error_name = "Could not get the card number input text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtMonth = self.wait.until(ec.visibility_of_element_located((By.ID, "month")))
        except Exception as e:
            error_name = "Could not get the Month input text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtYear = self.wait.until(ec.visibility_of_element_located((By.ID, "year")))
        except Exception as e:
            error_name = "Could not get the Year input text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtNameOnCard = self.wait.until(ec.visibility_of_element_located((By.ID, "nameOnCard")))
        except Exception as e:
            error_name = "Could not get the name on card input text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtInvoice = self.wait.until(ec.visibility_of_element_located((By.ID, "invoice")))
        except Exception as e:
            error_name = "Could not get the invoice input text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnSbmt = self.wait.until(ec.visibility_of_element_located((By.ID, "btn-sbmt")))
        except Exception as e:
            error_name = "Could not get the btn-sbmt Button: {}".format(str(e))
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

    def fillform(self, amount=0, userType='standard'):
        error = list()
        fill = dict()
        self.cards = self.help.get_card()
        self.card = self.cards['cards'][self.cardType]

        method = "Sale"

        data = self.help.generate_info()

        if amount == 0:
            self.amount = data["amount"]
        else:
            self.amount = amount

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

        error += self.help.write_field_text(self.page, "Amount", self.txtAmount, self.amount)
        error += self.help.write_field_text(self.page, "Card Number", self.txtCardNumber, self.card)
        error += self.help.write_field_text(self.page, "month", self.txtMonth, self.month)
        error += self.help.write_field_text(self.page, "year", self.txtYear, self.year)
        error += self.help.write_field_text(self.page, "nameOnCard", self.txtNameOnCard, self.nameOnCard)

        error += self.help.write_field_text(self.page, "invoice", self.txtInvoice, self.invoice)

        try:
            self.txtCvv = self.wait.until(ec.visibility_of_element_located((By.ID, "cvv")))
        except Exception as e:
            error_name = "Could not get the CVV input text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.write_field_text(self.page, "cvv", self.txtCvv, self.cvv)

        #try:
        #    self.txtEmail = self.wait.until(ec.visibility_of_element_located((By.ID, "email")))
        #except Exception as e:
        #    error_name = "Could not get the invoice input text: {}".format(str(e))
        #    self.help.error_log(self.page, error_name)
        #    error.append(error_name)

       # error += self.help.write_field_text(self.page, "email", self.txtEmail, self.email)

        if userType != "california":
            try:
                self.txtZipCode = self.wait.until(ec.visibility_of_element_located((By.ID, "zipCode")))
            except Exception as e:
                error_name = "Could not get the zipCode input text: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.txtAddress = self.wait.until(ec.visibility_of_element_located((By.ID, "address")))
            except Exception as e:
                error_name = "Could not get the address input text: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            error += self.help.write_field_text(self.page, "address", self.txtAddress, self.address)
            error += self.help.write_field_text(self.page, "zipCode", self.txtZipCode, self.zip)


        if self.btnSbmt.get_attribute("disabled"):
            self.help.info_log(self.page, "The Button Submit is disabled")
        else:
            error += self.help.click_button(self.page, self.btnSbmt)
            if len(error) == 0:
                self.help.info_log(self.page, "Button Submit is clicked correctly")
            else:
                fill = self.help.make_error_list(self.driver, method, error)

        if len(error) == 0:
            self.help.info_log(self.page, "The fill form correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

