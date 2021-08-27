import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Check.voidActions import VoidActions


class ClickCheckVoidMerchant(dashBoardConditions):
    page = "Void page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = VoidActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
