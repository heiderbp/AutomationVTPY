import time

from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.menuPage import DashboardP
from PagesObject.Pages.Cards.creditPage import CreditPage


class creditActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Credit Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnCards()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = cardPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("Credit")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Credit -> ok.")

        self.form = CreditPage(self.driver, self.help)

    def actionsClickCmbMerchant(self):

        errorClicCmbMerchant = self.form.clickCmbMerchant()
        if len(errorClicCmbMerchant) != 0:
            self.error.append(errorClicCmbMerchant)
        time.sleep(2)