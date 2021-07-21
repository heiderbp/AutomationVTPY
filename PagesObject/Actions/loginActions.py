import time

import Helpers.Helps
from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.loginPage import LoginPage


class LoginActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Login Actions Page"

    def actionsLogin(self, user, password, mid):
        form = LoginPage(self.driver,self.help)

        fill = form.fillFrom(user,password, mid)
        if(len(fill)!=0):
            self.error.append(fill)

        clic = form.clicksubmitLogin()
        if (len(clic) != 0):
            self.error.append(clic)

    def actionsLogout(self):
        form1 = DashboardP(self.driver, self.help)
        form1.clickbtnAdministration()
        self.help.info_log(self.page,"Administration Menu was loads correctly.")
        # time.sleep(3)
        # form1.clickbtnCards()
        # self.help.info_log(self.page, "Menu Cards se cargo Correctamente.")
        # time.sleep(3)
        # form1.clickbtnCheck()
        # time.sleep(3)
        # form1.clickbtnGift()
        # time.sleep(3)
        # form1.clickbtnReports()
        # time.sleep(3)
        # form1.clickbtnAdministration()
        time.sleep(3)
        form2 = administrationPage(self.driver)
        # form2.clickSubmenuRoles()
        # time.sleep(1)
        # form2.clickSubmenuUser()
        # time.sleep(1)
        # form2.clickSubmenuMerchant()
        # time.sleep(1)
        # form2.clickSubmenuInvoiceTemplates()
        time.sleep(1)
        form2.clickSubmenu("MerchantParameters")
        time.sleep(1)
        # form2.clickSubmenuAccessControlList()
        # time.sleep(1)
        # form2.clickSubmenuCountriesAcl()
        frmClicProfile = form1.clickbtnProfile()
        if (len(frmClicProfile) != 0):
            self.error.append(frmClicProfile)

        frmClicLogout = form1.clickbtnLogout()
        if (len(frmClicLogout) != 0):
            self.error.append(frmClicLogout)



