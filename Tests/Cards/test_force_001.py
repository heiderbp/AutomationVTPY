import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Cards.forceActions import forceActions


class ClickCardsForceReferenceNumber(dashBoardConditions):
    page = "Reference Number page"

    def test_ClickReferenceNumber(self):
        self.name_test = "Click Textbox Reference Number"
        actions = forceActions(self.driver, self.help)
        actions.actionsClickTxtReferenceNumber()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
