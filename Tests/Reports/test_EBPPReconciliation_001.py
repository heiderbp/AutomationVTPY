import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Reports.EBPPReconciliationActions import EBPPReconciliationActions


class ClickReportsEBPPReconciliationDataSeries(dashBoardConditions):
    page = "EBPP Reconciliation page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = EBPPReconciliationActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
