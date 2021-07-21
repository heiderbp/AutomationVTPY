import time

from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Cards.forcePage import ForcePage


class forceActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Force Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnCards()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = cardPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("Force")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Force -> ok.")

        self.form = ForcePage(self.driver, self.help)

    def actionsClickTxtReferenceNumber(self):

        errorClicTxtReferenceNumber = self.form.clickTxtReferenceNumber()
        if len(errorClicTxtReferenceNumber) != 0:
            self.error.append(errorClicTxtReferenceNumber)
        time.sleep(2)