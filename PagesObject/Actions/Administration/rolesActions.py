import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.menuPage import MenuP
from PagesObject.Pages.Administration.rolesPage import RolesPage


class rolesActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Roles Actions Page"
        self.form = RolesPage(self.driver, self.help)

    def actionsClickSearch(self):

        self.menu = MenuP(self.driver, self.help)
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

        errorClicRoleSearch = self.form.clickRoleSearch()
        if len(errorClicRoleSearch) != 0:
            self.error.append(errorClicRoleSearch)
        time.sleep(2)

    def actionsSearchRol(self, text):
       # self.form = RolesPage(self.driver, self.help)
        errorWriteRoleSearch = self.form.writeRoleSearch(text)

        txtResultRol = self.form.getTxtResultRol()

        if txtResultRol == "No matching records found":
            result = False
        else:
            result = True

        if len(errorWriteRoleSearch) != 0:
            self.error.append(errorWriteRoleSearch)

        return result

    def actionsNewRol(self, text):
        #self.form = RolesPage(self.driver, self.help)

        error = self.form.clickRowSelect()
        if len(error) != 0:
            self.error.append(error)

        error = self.form.writeRoleName(text)
        if len(error) != 0:
            self.error.append(error)

        error = self.form.fillform()
        if len(error) != 0:
            self.error.append(error)

        errorClicSave = self.form.clicksave()
        if len(errorClicSave) != 0:
            self.error.append(errorClicSave)

    def actionsDeleteRol(self):
       # self.form = RolesPage(self.driver, self.help)

        error = self.form.clickDeleteRol()
        if len(error) != 0:
            self.error.append(error)

    def actionsEditRol(self):
        # self.form = RolesPage(self.driver, self.help)

        error = self.form.clickEditRol()
        if len(error) != 0:
            self.error.append(error)

        error = self.form.click_random_check_debit_credit_card()
        if len(error) != 0:
            self.error.append(error)

        errorClicSave = self.form.clicksave()
        if len(errorClicSave) != 0:
            self.error.append(errorClicSave)


