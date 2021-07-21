from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from PagesObject.Locators import Locators


class DashboardP:
    def __init__(self, driver, helps, flag=True):
  ##  def __init__(self, driver, flag=True):
        self.driver = driver
        self.help = helps

        self.page = "Dashboard Page"

        error = list()
        self.error = dict()

        self.wait = WebDriverWait(self.driver, 5)

        self.btnProfile = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#app>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large')))

        if flag:
            try:
                self.menuAdministration = self.driver.find_element(By.CSS_SELECTOR, Locators.menu.replace("MENU", "2"))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuCards = self.driver.find_element(By.CSS_SELECTOR, Locators.menu.replace("MENU", "3"))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuCheck = self.driver.find_element(By.CSS_SELECTOR, Locators.menu.replace("MENU", "4"))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuGift = self.driver.find_element(By.CSS_SELECTOR, Locators.menu.replace("MENU", "5"))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            try:
                self.menuReports = self.driver.find_element(By.CSS_SELECTOR, Locators.menu.replace("MENU", "6"))
            except Exception as e:
                error_name = "Could not get the Administration menu item: {}".format(str(e))
                self.help.error_log(self.page, error_name)
                error.append(error_name)

            if len(error) == 0:
                self.help.info_log(self.page, "Items Obtained")


    def clickbtnProfile(self):
        error = list()
        fill = dict()
        method = "Desboard Button Profile"
      ##  error += self.btnProfile.click()
        error += self.help.click_button(self.page, self.btnProfile)
        if len(error) == 0:
            self.help.info_log(self.page, "Profile is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill


    def clickbtnLogout(self):
        error = list()
        fill = dict()
        method = "Desboard Button Logout"
        self.btnLogout = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#app>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(3)')))
        error += self.help.click_button(self.page, self.btnLogout)
       ## error += self.btnLogout.click()
        if len(error) == 0:
            self.help.info_log(self.page, "Logout is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickbtnAdministration(self):
        error = list()
        fill = dict()
        method = "Desboard Button Administration"
       ## self.menuAdministration.click()
        error += self.help.click_button(self.page, self.menuAdministration)
        if len(error) == 0:
            self.help.info_log(self.page, "Administration is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickbtnCards(self):
        error = list()
        fill = dict()
        method = "Desboard Button Cards"
      ##  self.menuCards.click()
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
      ##  self.menuCheck.click()
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
      ##  self.menuGift.click()
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
       ## self.menuReports.click()
        error += self.help.click_button(self.page, self.menuReports)
        if len(error) == 0:
            self.help.info_log(self.page, "Reports is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill


  #  def clickbtnRoles(self):
  #      self.Menu.click()
  #      self.subMenu.click()


# try:
#     self.subMenu = self.driver.find_element(By.CSS_SELECTOR,
#                                             Locators.subMenu.replace("SUBMENU", "1").replace("MENU", "2"))
#
# except Exception as e:
#     error_name = "Could not get the Roles sub menu item: {}".format(str(e))
#     ## self.help.error_log(self.page, error_name)
#     error.append(error_name)