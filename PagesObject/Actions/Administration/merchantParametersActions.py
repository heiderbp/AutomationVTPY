import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Administration.merchantParametersPage import MerchantParametersPage


class merchantParametersActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Merchant Parameters Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnAdministration()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "Administration Menu was loads correctly.")

        self.submenu = administrationPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("MerchantParameters")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Merchant Parameters is ok.")

        self.form = MerchantParametersPage(self.driver, self.help)

    def actionsModifyMerchantParametersAvs(self):

        errorClicTabAvs = self.form.clicktabavs()
        if len(errorClicTabAvs) != 0:
            self.error.append(errorClicTabAvs)
        time.sleep(2)
        errorClicChksTabAvs = self.form.clickcheckavs()
        if len(errorClicChksTabAvs) != 0:
            self.error.append(errorClicChksTabAvs)

    def actionsModifyMerchantParametersZip(self):

        errorClicTabZip = self.form.clicktabzip()
        if len(errorClicTabZip) != 0:
            self.error.append(errorClicTabZip)
        time.sleep(2)
        errorClicChcksTabZip = self.form.clickcheckzip()
        if len(errorClicChcksTabZip) != 0:
            self.error.append(errorClicChcksTabZip)

    def actionsModifyMerchantParametersCvv(self):

        errorClicTabCvv = self.form.clicktabcvv()
        if len(errorClicTabCvv) != 0:
            self.error.append(errorClicTabCvv)
        time.sleep(2)
        errorClicChcksTabCvv = self.form.clickcheckcvv()
        if len(errorClicChcksTabCvv) != 0:
            self.error.append(errorClicChcksTabCvv)

    def saveform(self):
        errorClicSave = self.form.clicksave()
        if len(errorClicSave) != 0:
            self.error.append(errorClicSave)
