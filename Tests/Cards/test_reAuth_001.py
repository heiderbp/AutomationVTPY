import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Cards.reAuthActions import ReAuthActions


class ClickCardsForceReferenceNumber(dashBoardConditions):
    page = "Reference Number page"

    def test_ClickReferenceNumber(self):
        self.name_test = "Click Textbox Reference Number"
        actions = ReAuthActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
