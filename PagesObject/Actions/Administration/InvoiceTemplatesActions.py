import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.menuPage import DashboardP
from PagesObject.Pages.Cards.salePage import SalePage


class invoiceTemplatesActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Invoice Templates Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnAdministration()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = administrationPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("InvoiceTemplates")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Users -> ok.")

        self.form = SalePage(self.driver, self.help)

    def actionsClickSale(self):

        errorClicSale = self.form.clickCmbSale()
        if len(errorClicSale) != 0:
            self.error.append(errorClicSale)
        time.sleep(2)