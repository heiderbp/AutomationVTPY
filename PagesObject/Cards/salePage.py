import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class SalePage:
    def __init__(self, driver, helps, card=str()):
        self.driver = driver
        self.help = helps
        self.page = "Sale Page"
        self.cardType = card


        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Cards', 'sale')

        try:
            self.cmbMerchant = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elements['cmbMerchant']['css'])))
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
            self.txtRadioMOTO = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#radioButtonTypes>div:nth-child(2)")))
        except Exception as e:
            error_name = "Could not get the MOTO Radio Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtRadioSale = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#radioButtonTypes>div:nth-child(1)")))
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
        method = "Sale"
        error += self.help.click_button(self.page, self.cmbMerchant)

        try:
            self.ItemsCmbMerchant = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.help.get_element('Cards', 'sale')['cmbMerchant']['css'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if len(error) == 0:
            self.help.info_log(self.page, "The Combo box Merchant is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def check_exists_by_css_selector(self, css_selector):
        try:
            time.sleep(1)
            self.driver.find_element_by_css_selector(css_selector)
        except NoSuchElementException:
            return False
        return True

    def fillElementsTicket(self):
        fill = dict()
        error = list()

        try:
            self.elementsTicket = self.driver.find_elements_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(2)>div>div")
        except Exception as e:
            error_name = "Could not get table html: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        for a in range(2, len(self.elementsTicket)-1):
            countElementsDiv = self.driver.find_elements_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(" + str(a) + ")>div")
            if len(countElementsDiv) > 0:
                description = self.driver.find_element_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(" + str(a) + ")>div>span:nth-child(1)").text
                value = self.driver.find_element_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(" + str(a) + ")>div>span:nth-child(2)").text
                fill[description] = value

        try:
            self.elementsCustomerInfo = self.driver.find_elements_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(1)>div")
        except Exception as e:
            error_name = "Could not get table html: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        for a in range(1, len(self.elementsCustomerInfo)):
            countElementsDiv = self.driver.find_elements_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(1)>div>div:nth-child(" + str(a) + ")>div>span")
            print(len(countElementsDiv))
            if len(countElementsDiv) > 0:
                description = self.driver.find_element_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(1)>div>div:nth-child(" + str(a) + ")>div>span:nth-child(1)").text
                value = self.driver.find_element_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(1)>div>div:nth-child(" + str(a) + ")>div>span:nth-child(2)").text
                fill[description] = value

        #fill['Name on Card:'] = self.driver.find_elements_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(1)>div.layout.column.pa-2.text-sm-left>div").text
        #print(len(self.elementsCustomerInfo))

        return fill

    def getElementTicket(self, parameter):
        error = list()
        fill = dict()
        method = "Sale"

        try:
            self.elementsTicket = self.driver.find_elements_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(2)>div>div")
        except Exception as e:
            error_name = "Could not get the Combo box cmbMerchant: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        print(len(self.elementsTicket))

        for a in range(2, len(self.elementsTicket)):
            countElementsDiv = self.driver.find_elements_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(" + str(a) + ")>div")
            if len(countElementsDiv) > 0:
                title = self.driver.find_element_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(" + str(a) + ")>div>span:nth-child(1)").text
                if title == parameter:
                    idTransaccion = self.driver.find_element_by_css_selector("#invoice-area>div>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(" + str(a) + ")>div>span:nth-child(2)").text

        return idTransaccion

    def clickButtonDone(self):
        error = list()
        method = "Sale"
        fill = dict()

        try:
            self.btnDone = self.wait.until(ec.visibility_of_element_located((By.ID, "done")))
        except Exception as e:
            error_name = "Could not get the Done Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnDone)
        if len(error) == 0:
            self.help.info_log(self.page, "Button Submit is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill


    def fillform(self, amount=0, userType = 'standard', customEmail = ""):
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

        if self.cardType == "expired":
            self.month = "04"
            self.year = "18"
        else:
            self.month = data["month"]
            self.year = data["year"]

        self.nameOnCard = data["name"]
        self.invoice = data["invoice"]

        if customEmail == "":
            self.email = data["email"]
        else:
            self.email = customEmail

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


        try:
            self.txtEmail = self.wait.until(ec.visibility_of_element_located((By.ID, "email")))
        except Exception as e:
            error_name = "Could not get the invoice input text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.write_field_text(self.page, "email", self.txtEmail, self.email)

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

    def actionsClickCmbMerchant(self):
        self.clickCmbMerchant()

    def fillformdecline(self):
        self.fillform(self.cardType, 248)