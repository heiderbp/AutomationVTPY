import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Gift.activateActions import ActivateActions


class ClickGiftActivateMerchant(dashBoardConditions):
    page = "Activate page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = ActivateActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
