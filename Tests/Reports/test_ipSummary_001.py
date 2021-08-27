import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Reports.ipSummaryActions import IPSummaryActions


class ClickReportsIPSummaryDataSeries(dashBoardConditions):
    page = "IP Summary page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = IPSummaryActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
