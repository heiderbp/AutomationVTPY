import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Check.guaranteeActions import GuaranteeActions


class ClickCheckGuaranteeMerchant(dashBoardConditions):
    page = "Guarantee page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = GuaranteeActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
