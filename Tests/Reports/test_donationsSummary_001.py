import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Reports.donationsSummaryActions import DonationsSummaryActions


class ClickReportsDonationsSummaryDataSeries(dashBoardConditions):
    page = "Donations Summary page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = DonationsSummaryActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
