import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.menuPage import DashboardP
from PagesObject.Pages.Administration.countriesAclPage import CountriesACLPage


class countriesAclActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Countries Acl Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnAdministration()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = administrationPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("CountriesAcl")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Countries Acl -> ok.")

        self.form = CountriesACLPage(self.driver, self.help)

    def actionsClickChkCountriesACL(self):

        errorClicCountriesACL = self.form.clickChkAllowedCountries()
        if len(errorClicCountriesACL) != 0:
            self.error.append(errorClicCountriesACL)
        time.sleep(2)