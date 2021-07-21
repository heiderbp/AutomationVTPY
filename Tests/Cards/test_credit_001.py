import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Cards.creditActions import creditActions


class ClickCardsCreditMerchant(dashBoardConditions):
    page = "Credit page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = creditActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
