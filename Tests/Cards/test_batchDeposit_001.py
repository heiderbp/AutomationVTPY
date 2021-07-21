import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Cards.batchDepositActions import batchDepositActions


class ClickCardsBatchDeposit(dashBoardConditions):
    page = "Batch Deposit page"

    def test_ClickBatchDepositYes(self):
        self.name_test = "Click Yes"
        actions = batchDepositActions(self.driver, self.help)
        actions.actionsClickBtnYes()
        self.help.info_log(self.page, self.name_test + " Yes")
        time.sleep(5)
