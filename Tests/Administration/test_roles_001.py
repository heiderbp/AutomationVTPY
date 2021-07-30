import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.loginActions import LoginActions
from PagesObject.Actions.Administration.rolesActions import rolesActions


class ClickSearch(dashBoardConditions):
    page = "Roles test page"

    def test_ClickSearch(self):
        self.name_test = "Click Search textbox"
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')


        actions = rolesActions(self.driver, self.help)

        actions.actionsClickSearch()
        self.help.info_log(self.page, self.name_test + " Search")

        time.sleep(5)
      #  self.error = actions.error
