import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Reports.cashSummaryActions import CashSummaryActions


class ClickReportsCashSummaryDataSeries(dashBoardConditions):
    page = "Cash Summary page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = CashSummaryActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(1)
        time.sleep(5)
