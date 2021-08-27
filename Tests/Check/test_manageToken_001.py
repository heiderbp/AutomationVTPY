import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Check.manageTokenActions import ManageTokenActions


class ClickCheckManageTokenMerchant(dashBoardConditions):
    page = "Manage Token page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = ManageTokenActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
