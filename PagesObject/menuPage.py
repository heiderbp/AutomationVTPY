from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from PagesObject.administrationPage import administrationPage
from PagesObject.cardPage import cardPage
from PagesObject.checkPage import checkPage
from PagesObject.giftPage import giftPage
from PagesObject.reportsPage import reportsPage


from PagesObject.Locators import Locators


class MenuP:
    def __init__(self, driver, helps, flag=True):
        self.driver = driver
        self.help = helps

        self.page = "Menu Page"

        error = list()
        self.error = dict()

        self.wait = WebDriverWait(self.driver, 5)

        self.btnProfile = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#app>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large')))

        if flag:
            try:
                self.menuHome = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>nav>div.v-navigation-drawer__content>div>div:nth-child(1)")))
            except Exception as e:
                error_name = "Could not get the Home menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuAdministration = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>nav>div.v-navigation-drawer__content>div>div:nth-child(2)>div")))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuCards = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, Locators.menu.replace("MENU", "3"))))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuCheck = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, Locators.menu.replace("MENU", "4"))))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuGift = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, Locators.menu.replace("MENU", "5"))))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuReports = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, Locators.menu.replace("MENU", "6"))))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            if len(error) == 0:
                self.help.info_log(self.page, "Items Obtained")

    def clickbtnAdministration(self):
        error = list()
        fill = dict()
        method = "Desboard Button Administration"

        self.menuAdministration.click()
        if len(error) == 0:
            self.help.info_log(self.page, "Administration is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickbtnCards(self):
        error = list()
        fill = dict()
        method = "Desboard Button Cards"

        error += self.help.click_button(self.page, self.menuCards)
        if len(error) == 0:
            self.help.info_log(self.page, "Cards is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickbtnCheck(self):
        error = list()
        fill = dict()
        method = "Desboard Button Check"

        error += self.help.click_button(self.page, self.menuCheck)
        if len(error) == 0:
            self.help.info_log(self.page, "Check is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickbtnGift(self):
        error = list()
        fill = dict()
        method = "Desboard Button Gift"

        error += self.help.click_button(self.page, self.menuGift)
        if len(error) == 0:
            self.help.info_log(self.page, "Gift is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickbtnReports(self):
        error = list()
        fill = dict()
        method = "Desboard Button Reports"

        error += self.help.click_button(self.page, self.menuReports)
        if len(error) == 0:
            self.help.info_log(self.page, "Reports is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def actionsMenu(self, name_menu, name_submenu):

        if name_menu == "Administration":
            self.clickbtnAdministration()
            admin = administrationPage(self.driver, self.help)
            admin.clickSubmenu(name_submenu)

        elif name_menu == "Cards":
            self.clickbtnCards()
            card = cardPage(self.driver, self.help)
            card.clickSubmenu(name_submenu)

        elif name_menu == "Check":
            self.menuCheck()
            check = checkPage(self.driver, self.help)
            check.clickSubmenu(name_submenu)

        elif name_menu == "Gift":
            self.clickbtnGift()
            gift = giftPage(self.driver, self.help)
            gift.clickSubmenu(name_submenu)
        elif name_menu == "Reports":
            self.clickbtnReports()
            reports = reportsPage(self.driver, self.help)
            reports.clickSubmenu(name_submenu)

        self.help.info_log(self.page, name_submenu + " Menu was loads correctly.")
