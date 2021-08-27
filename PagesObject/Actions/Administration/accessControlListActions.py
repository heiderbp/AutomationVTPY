import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.menuPage import DashboardP
from PagesObject.Pages.Administration.accessControlListPage import AccessControlListPage


class ipToAllowedActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Access Control List Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnAdministration()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = administrationPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("AccessControlList")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Users -> ok.")

        self.form = AccessControlListPage(self.driver, self.help)

    def actionsClickIpToAllowed(self):

        errorclickTxtIpToAllowed = self.form.clickTxtIpToAllowed()
        if len(errorclickTxtIpToAllowed) != 0:
            self.error.append(errorclickTxtIpToAllowed)
        time.sleep(2)