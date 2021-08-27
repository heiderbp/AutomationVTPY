import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Cards.lightRecurringActions import LightRecurringActions


class ClickCardsLightRecurringCmbMerchant(dashBoardConditions):
    page = "Light Recurring page"

    def test_ClickCmbMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = LightRecurringActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + ".")
        time.sleep(5)
