import time

from PagesObject.Pages.checkPage import checkPage
from PagesObject.Pages.menuPage import DashboardP
from PagesObject.Pages.Check.useTokenPage import UseTokenPage


class UseTokenActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Use Token Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnCheck()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = checkPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("UseToken")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Auth -> ok.")

        self.form = UseTokenPage(self.driver, self.help)

    def actionsClickCmbMerchant(self):

        errorClicCmbMerchant = self.form.clickTxtAbaNumber()
        if len(errorClicCmbMerchant) != 0:
            self.error.append(errorClicCmbMerchant)
        time.sleep(2)