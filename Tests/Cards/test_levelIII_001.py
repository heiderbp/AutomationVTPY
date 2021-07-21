import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Cards.levelIIActions import LevelIiiActions


class ClickCardsLevelIiiCmbTemplate(dashBoardConditions):
    page = "Reference Number page"

    def test_ClickCmbTemplate(self):
        self.name_test = "Click Combo Template"
        actions = LevelIiiActions(self.driver, self.help)
        actions.actionsClickCmbTemplate()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
