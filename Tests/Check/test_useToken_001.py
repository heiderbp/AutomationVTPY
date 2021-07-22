import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Check.useTokenActions import UseTokenActions


class ClickCheckUseTokenMerchant(dashBoardConditions):
    page = "Use Token page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = UseTokenActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
