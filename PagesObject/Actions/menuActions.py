import time

from PagesObject.Pages.menuPage import MenuP
from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.checkPage import checkPage
from PagesObject.Pages.giftPage import giftPage
from PagesObject.Pages.reportsPage import reportsPage


class MenuActions:

    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Menu Actions Page"
        self.login = MenuP(self.driver, self.help)
        self.error_menu = dict()

    def actionsMenu(self, name_menu, name_submenu):

        if name_menu == "Administration":

            self.menu = MenuP(self.driver, self.help)
            self.error_menu = self.menu.clickbtnAdministration()

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)

            admin = administrationPage(self.driver, self.help)
            self.error_menu = admin.clickSubmenu(name_submenu)

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)

        elif name_menu == "Cards":
            self.menu = MenuP(self.driver, self.help)
            self.error_menu = self.menu.clickbtnCards()

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)

            card = cardPage(self.driver, self.help)
            self.error_menu = card.clickSubmenu(name_submenu)

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)

        elif name_menu == "Check":
            self.menu = MenuP(self.driver, self.help)
            self.error_menu = self.menu.menuCheck()

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)

            check = checkPage(self.driver, self.help)
            self.error_menu += check.clickSubmenu(name_submenu)

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)
        elif name_menu == "Gift":
            self.menu = MenuP(self.driver, self.help)
            self.error_menu = self.menu.clickbtnGift()

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)

            gift = giftPage(self.driver, self.help)
            self.error_menu = gift.clickSubmenu(name_submenu)

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)
        elif name_menu == "Reports":
            self.menu = MenuP(self.driver, self.help)
            self.error_menu = self.menu.clickbtnReports()

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)

            reports = reportsPage(self.driver, self.help)
            self.error_menu = reports.clickSubmenu(name_submenu)

            if len(self.error_menu) != 0:
                self.error.append(self.error_menu)

        self.help.info_log(self.page, name_submenu + " Menu was loads correctly.")
