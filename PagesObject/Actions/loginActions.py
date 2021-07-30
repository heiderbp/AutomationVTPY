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

    def actionsLogin(self, userType):

        mid = self.help.get_parameters()["mid"][userType]
        user = self.help.get_parameters()["users"][userType]
        password = self.help.get_parameters()["passwords"][userType]

        login = LoginPage(self.driver, self.help)
        fill = login.fillFrom(user, password, mid)

        if(len(fill)!=0):
            self.error.append(fill)

        clic = login.clicksubmitLogin()

        if (len(clic) != 0):
            self.error.append(clic)

    def actionsLogout(self):
        form1 = DashboardP(self.driver, self.help)
#        form1.clickbtnAdministration()
 #       self.help.info_log(self.page,"Administration Menu was loads correctly.")
  #      time.sleep(3)
   #     form2 = administrationPage(self.driver)

   #     time.sleep(1)
   #     form2.clickSubmenu("MerchantParameters")
   #     time.sleep(1)

        frmClicProfile = form1.clickbtnProfile()
        if (len(frmClicProfile) != 0):
            self.error.append(frmClicProfile)

        frmClicLogout = form1.clickbtnLogout()
        if (len(frmClicLogout) != 0):
            self.error.append(frmClicLogout)



