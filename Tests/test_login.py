import time
from Conditions.loginConditions import LoginConditions
from PagesObject.Actions.loginActions import LoginActions


class Test0001(LoginConditions):
    page = "login test Page"

    def test_0001(self):
        self.name_test = "Log in to the application successfully"
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(2)

    def test_0002(self):
        self.name_test = "Log in to the application successfully providing a username containing valid special characters."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('usrSpecialChar')
        time.sleep(2)

    def test_0003(self):
        self.name_test = "Log in to the application successfully after changing an already expired password."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('usrChangeExpiredPwd')
        time.sleep(2)

    def test_0004(self):
        self.name_test = "Attempt to log in to the application providing invalid credentials."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('invalid')
        time.sleep(2)