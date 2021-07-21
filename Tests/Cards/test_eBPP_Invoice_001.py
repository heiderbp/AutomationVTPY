import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Cards.eBPPInvoiceActions import EBPPInvoiceActions


class ClickCardsEBPPInvoiceName(dashBoardConditions):
    page = "EBPP Invoice page"

    def test_ClickEBPPInvoiceName(self):
        self.name_test = "Click textbox name"
        actions = EBPPInvoiceActions(self.driver, self.help)
        actions.actionsClickTxtName()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
