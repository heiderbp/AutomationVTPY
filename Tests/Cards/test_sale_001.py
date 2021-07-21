import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Cards.saleActions import saleActions


class ClickCardsSaleMerchant(dashBoardConditions):
    page = "Sale page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = saleActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
