import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Administration.usersPage import UsersPage


class usersActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Users Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnAdministration()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = administrationPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("Users")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Users -> ok.")

        self.form = UsersPage(self.driver, self.help)

    def actionsClickSearch(self):

        errorClicUsersSearch = self.form.clickUsersSearch()
        if len(errorClicUsersSearch) != 0:
            self.error.append(errorClicUsersSearch)
        time.sleep(2)