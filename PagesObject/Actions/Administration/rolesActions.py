import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Administration.rolesPage import RolesPage


class rolesActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Roles Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnAdministration()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "Role Menu was loads correctly.")

        self.submenu = administrationPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("Roles")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Roles -> ok.")

        self.form = RolesPage(self.driver, self.help)

    def actionsClickSearch(self):

        errorClicRoleSearch = self.form.clickRoleSearch()
        if len(errorClicRoleSearch) != 0:
            self.error.append(errorClicRoleSearch)
        time.sleep(2)
