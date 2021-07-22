import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Reports.transactionsActions import TransactionsActions


class ClickReportsTransactionsDataSeries(dashBoardConditions):
    page = "Transactions page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = TransactionsActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
