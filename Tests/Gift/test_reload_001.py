import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Gift.reloadActions import ReloadActions


class ClickCardsAuthMerchant(dashBoardConditions):
    page = "Reload page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = ReloadActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
