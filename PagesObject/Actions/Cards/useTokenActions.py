import time

from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Cards.useTokenPage import UseTokenPage


class UseTokenActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Use Token Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnCards()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = cardPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("UseToken")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Auth -> ok.")

        self.form = UseTokenPage(self.driver, self.help)

    def actionsClickCmbMerchant(self):

        errorClicCmbMerchant = self.form.clickTxtLastFourDigits()
        if len(errorClicCmbMerchant) != 0:
            self.error.append(errorClicCmbMerchant)
        time.sleep(2)