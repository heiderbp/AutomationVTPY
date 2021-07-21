import time

from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Cards.batchDepositPage import batchDepositPage


class batchDepositActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Batch Deposit Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnCards()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = cardPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("BatchDeposit")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Auth -> ok.")

        self.form = batchDepositPage(self.driver, self.help)

    def actionsClickBtnYes(self):
        errorClicBtnYes = self.form.clickBtnYes()
        if len(errorClicBtnYes) != 0:
            self.error.append(errorClicBtnYes)
        time.sleep(2)

    def actionsClickBtnNo(self):
        errorClicBtnNo = self.form.clickBtnNo()
        if len(errorClicBtnNo) != 0:
            self.error.append(errorClicBtnNo)
        time.sleep(2)