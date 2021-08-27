import time

from PagesObject.Pages.giftPage import giftPage
from PagesObject.Pages.menuPage import DashboardP
from PagesObject.Pages.Gift.reloadPage import ReloadPage


class ReloadActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Reload Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnGift()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = giftPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("Reload")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Reload -> ok.")

        self.form = ReloadPage(self.driver, self.help)

    def actionsClickCmbMerchant(self):

        errorClicCmbMerchant = self.form.clickTxtAmount()
        if len(errorClicCmbMerchant) != 0:
            self.error.append(errorClicCmbMerchant)
        time.sleep(2)