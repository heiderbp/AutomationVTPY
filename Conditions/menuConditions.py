from Conditions.GeneralConditions.DashboardGeneralConditions import dashboardGC


class dashBoardConditions(dashboardGC):

    def tearDown(self) -> None:
        self.help.tear_down(self.name_test, self.page, self.error, self.mid)
