import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Reports.geolocationActions import GeolocationActions


class ClickReportsGeolocationDataSeries(dashBoardConditions):
    page = "Geolocation page"

    def test_ClickDataSeries(self):
        self.name_test = "Click Combobox Data Series"
        actions = GeolocationActions(self.driver, self.help)
        actions.actionsClickCmbDataSeries()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
