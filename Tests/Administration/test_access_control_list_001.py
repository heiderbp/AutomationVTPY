import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Administration.accessControlListActions import ipToAllowedActions


class ClickSearch(dashBoardConditions):
    page = "Access Control List test page"

    def test_ClickIpToAllowed(self):
        self.name_test = "Click Search textbox"

        actions = ipToAllowedActions(self.driver, self.help)

        actions.actionsClickIpToAllowed()
        self.help.info_log(self.page, self.name_test + " Search")

        time.sleep(5)
      #  self.error = actions.error

    def test_ClickIpToAllowed_002(self):
        self.name_test = "Click Search textbox"

        actions = ipToAllowedActions(self.driver, self.help)

        actions.actionsClickIpToAllowed()
        self.help.info_log(self.page, self.name_test + " Search")

        time.sleep(5)
      #  self.error = actions.error