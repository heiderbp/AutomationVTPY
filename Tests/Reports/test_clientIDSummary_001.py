import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Reports.clientIDSummaryActions import ClientIDSummaryActions


class ClickReportsClientIDSummaryDataSeries(dashBoardConditions):
    page = " Client ID Summary page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = ClientIDSummaryActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
