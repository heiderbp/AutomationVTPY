import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Cards.useTokenActions import UseTokenActions


class ClickCardsUseTokenCmbMerchant(dashBoardConditions):
    page = "Use Token test page"

    def test_ClickCmbMerchant(self):
        self.name_test = "Click ComboBox Merchant"
        actions = UseTokenActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Select")
        time.sleep(5)
