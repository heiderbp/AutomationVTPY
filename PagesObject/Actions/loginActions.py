import time

import Helpers.Helps
from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.menuPage import MenuP
from PagesObject.Pages.loginPage import LoginPage


class LoginActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Login Actions Page"
        self.login = LoginPage(self.driver, self.help)


    def actionsResetPassword(self,userType):
        errorClickResetPwd = self.login.clickResetPassword(userType)
        if len(errorClickResetPwd) != 0:
            self.error.append(errorClickResetPwd)


    def actionsLogin(self, userType):
        mid = self.help.get_parameters()["mid"][userType]
        user = self.help.get_parameters()["users"][userType]
        password = self.help.get_parameters()["passwords"][userType]
        fill = self.login.fillFrom(user, password, mid)

        if(len(fill)!=0):
            self.error.append(fill)

        click = self.login.clicksubmitLogin()

        if (len(click) != 0):
            self.error.append(click)

    def actionsLoginNewPasswordCancel(self, userType, pw):
        mid = self.help.get_parameters()["mid"][userType]
        user = self.help.get_parameters()["users"][userType]
        password = pw
        fill = self.login.fillFrom(user, password, mid)

        if (len(fill) != 0):
            self.error.append(fill)

        clic = self.login.clicksubmitLoginNewPasswordCancel()

        if (len(clic) != 0):
            self.error.append(clic)

    def actionsLoginNewPassword(self, userType, pw, new_pw, repeat_new_pw):
        mid = self.help.get_parameters()["mid"][userType]
        user = self.help.get_parameters()["users"][userType]
        password = pw
        fill = self.login.fillFrom(user, password, mid)

        if (len(fill) != 0):
            self.error.append(fill)

        clic = self.login.clicksubmitLoginNewPassword(new_pw,repeat_new_pw)

        if (len(clic) != 0):
            self.error.append(clic)




