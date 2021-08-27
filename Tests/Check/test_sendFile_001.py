import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Check.sendFileActions import SendFileActions


class ClickCheckSendFileMerchant(dashBoardConditions):
    page = "Send File page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = SendFileActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
