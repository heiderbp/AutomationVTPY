import time

from Conditions.loginConditions import LoginConditions
from PagesObject.Actions.loginActions import LoginActions


class Test0001(LoginConditions):
    page = "login test Page"

    """ def test_0001(self):
        actions = LoginActions(self.driver)
        actions.actions('hbedoya','Cenpos@541','30000720')

    def test_0002(self):
        actions = LoginActions(self.driver)
        actions.actions('hbedoya','Cenpos@54','30000720') """
    def test_00011(self):
        actions = LoginActions(self.driver, self.help)
        actions.actionsLogin('hbedoya', 'Cenpos@5', '30000720')
        actions.actionsLogout()
        time.sleep(5)

    # def test_00003(self):
    #     actions = LoginActions(self.driver, self.help)
    #     actions.actionsLogin('hbedoya', 'Cenpos@54', '300007201')
    #     self.help.info_log(self.page,"Test username ok password ok MID bad.")
    #     time.sleep(5)
    #
    # def test_00004(self):
    #     actions = LoginActions(self.driver, self.help)
    #     actions.actionsLogin('hbedoya1', 'Cenpos@54', '30000720')
    #     self.help.info_log(self.page,"Test username bad password ok MID ok.")
    #     time.sleep(5)
    #
    # def test_00005(self):
    #     actions = LoginActions(self.driver, self.help)
    #     actions.actionsLogin('hbedoya', 'Cenpos@541', '30000720')
    #     self.help.info_log(self.page,"Test username ok password bad MID ok.")
    #     time.sleep(5)
    #
    # def test_00006(self):
    #     actions = LoginActions(self.driver, self.help)
    #     actions.actionsLogin('hbedoya1', 'Cenpos@541', '30000720')
    #     self.help.info_log(self.page,"Test username bad password bad MID ok.")
    #     time.sleep(5)
    #
    # def test_00007(self):
    #     actions = LoginActions(self.driver, self.help)
    #     actions.actionsLogin('hbedoya1', 'Cenpos@54', '300007201')
    #     self.help.info_log(self.page,"Test username bad password ok MID bad.")
    #     time.sleep(5)

    # def test_00008(self):
    #     self.name_test = "Test username ok password bad MID bad."
    #     actions = LoginActions(self.driver, self.help)
    #
    #     actions.actionsLogin(self.user, self.password, self.mid)
    #     ## actions.actionsLogin("hbedoya", "Cenpos@5", "30000720")
    #     self.help.info_log(self.page,self.name_test)
    #     time.sleep(5)
    #     self.error = actions.error
