import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Administration.usersActions import usersActions


class ClickSearch(dashBoardConditions):
    page = "Users test page"

    def test_ClickSearch(self):
        self.name_test = "Click Search textbox"

        actions = usersActions(self.driver, self.help)

        actions.actionsClickSearch()
        self.help.info_log(self.page, self.name_test + " Search")

        time.sleep(5)
      #  self.error = actions.error