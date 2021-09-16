import time

from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.Cards.salePage import SalePage


class saleActions:
    def __init__(self, driver, helps, card=str()):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.cardType = card

        self.page = "Sale Actions Page"

        self.form = SalePage(self.driver, self.help)


    def actionsClickCmbMerchant(self):

        errorClicCmbMerchant = self.form.clickCmbMerchant()
        if len(errorClicCmbMerchant) != 0:
            self.error.append(errorClicCmbMerchant)

    def fillform(self):
        error = self.form.fillform(self.cardType)

        if len(error) != 0:
            self.error.append(error)

    def fillformdecline(self):
        error = self.form.fillform(self.cardType,248)

        if len(error) != 0:
            self.error.append(error)



