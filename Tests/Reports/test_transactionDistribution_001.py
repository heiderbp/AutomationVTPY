import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Reports.transactionDistributionActions import TransactionDistributionActions


class ClickReportsTransactionDistributionDataSeries(dashBoardConditions):
    page = "Transaction Distribution page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = TransactionDistributionActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
