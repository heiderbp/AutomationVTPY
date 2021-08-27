import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Cards.authActions import authActions


class ClickCardsAuthMerchant(dashBoardConditions):
    page = "Auth page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = authActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
