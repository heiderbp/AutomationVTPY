import time

from PagesObject.Pages.reportsPage import reportsPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Reports.cashSummaryPage import CashSummaryPage


class CashSummaryActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Cash Summary Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnReports()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = reportsPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("CashSummary")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Auth -> ok.")

        self.form = CashSummaryPage(self.driver, self.help)

    def actionsClickCmbDataSeries(self):

        errorClicCmbDataSeries = self.form.clickCmbDataSeries()
        if len(errorClicCmbDataSeries) != 0:
            self.error.append(errorClicCmbDataSeries)
        time.sleep(2)