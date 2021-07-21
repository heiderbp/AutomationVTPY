import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Cards.voiceActions import VoiceActions


class ClickCardsVoiceActionsCmbMerchant(dashBoardConditions):
    page = "Reference Number page"

    def test_ClickCmbMerchant(self):
        self.name_test = "Click Textbox Reference Number"
        actions = VoiceActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
