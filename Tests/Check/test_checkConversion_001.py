import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Check.checkConversionActions import CheckConversionActions


class ClickCheckCheckConversionMerchant(dashBoardConditions):
    page = "Check Conversion page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = CheckConversionActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
