import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Reports.supervisorActions import SupervisorActions


class ClickReportsSupervisorDataSeries(dashBoardConditions):
    page = "Supervisor page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = SupervisorActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
