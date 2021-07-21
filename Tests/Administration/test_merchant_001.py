import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Administration.merchantActions import merchantActions


class ClickMerchantData(dashBoardConditions):
    page = "Merchant test page"

    def test_MerchantData(self):
        self.name_test = "Click Tab Merchant Data"

        actions = merchantActions(self.driver, self.help)

        actions.actionsModifyMerchantData()
        self.help.info_log(self.page, self.name_test + " Tab")

        time.sleep(5)
      #  self.error = actions.error