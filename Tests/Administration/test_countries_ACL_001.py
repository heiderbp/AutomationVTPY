import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Administration.countriesAclActions import countriesAclActions


class ClickCountryACL(dashBoardConditions):
    page = "Countries Acl test page"

    def test_ClickAllowed(self):
        self.name_test = "Click checkbox"

        actions = countriesAclActions(self.driver, self.help)

        actions.actionsClickChkCountriesACL()
        self.help.info_log(self.page, self.name_test + " Search")

        time.sleep(5)
      #  self.error = actions.error