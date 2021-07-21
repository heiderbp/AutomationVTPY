import time

from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.deshboardPage import DashboardP
from PagesObject.Pages.Cards.levelIiiPage import LevelIiiPage


class LevelIiiActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Level III Actions Page"

        self.menu = DashboardP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnCards()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "User Menu was loads correctly.")

        self.submenu = cardPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("LevelIII")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Auth -> ok.")

        self.form = LevelIiiPage(self.driver, self.help)

    def actionsClickCmbTemplate(self):

        errorClicCmbTemplate = self.form.clickCmbTemplate()
        if len(errorClicCmbTemplate) != 0:
            self.error.append(errorClicCmbTemplate)
        time.sleep(2)