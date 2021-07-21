import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Reports.batchReportActions import BatchReportActions


class ClickReportsBatchDataSeries(dashBoardConditions):
    page = "Auth page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = BatchReportActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(1)
        time.sleep(5)
