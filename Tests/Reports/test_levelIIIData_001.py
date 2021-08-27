import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Reports.levelIIIDataActions import LevelIIIDataActions


class ClickReportsLevelIIIDataDataSeries(dashBoardConditions):
    page = "Level III Data page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = LevelIIIDataActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
