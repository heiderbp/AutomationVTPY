import time

from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.menuPage import DashboardP
from PagesObject.Pages.Cards.positiveCardPage import PositiveCardVerificationPage


class PositiveCardVerificationActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Positive Card Verification Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnCards()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = cardPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("PositiveCard")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Auth -> ok.")

        self.form = PositiveCardVerificationPage(self.driver, self.help)

    def actionsClickCmbMerchant(self):

        errorClicCmbMerchant = self.form.clickTxtCustomerCode()
        if len(errorClicCmbMerchant) != 0:
            self.error.append(errorClicCmbMerchant)
        time.sleep(2)