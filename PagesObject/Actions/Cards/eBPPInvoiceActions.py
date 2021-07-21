import time

from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Cards.eBPPInvoicePage import EBPPInvoicePage


class EBPPInvoiceActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "EBPP Invoice Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnCards()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = cardPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("EBPPInvoice")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Auth -> ok.")

        self.form = EBPPInvoicePage(self.driver, self.help)

    def actionsClickTxtName(self):

        errorClicTxtName = self.form.clickTxtNameOnCard()
        if len(errorClicTxtName) != 0:
            self.error.append(errorClicTxtName)
        time.sleep(2)