import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.menuPage import MenuP
from PagesObject.Pages.Administration.merchantPage import MerchantPage


class merchantActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Merchant Actions Page"

        self.menu = MenuP(self.driver, self.help)
        self.errormenu = self.menu.clickbtnAdministration()
        if len(self.errormenu) != 0:
            self.error.append(self.errormenu)
        self.help.info_log(self.page, "Administration Menu was loads correctly.")

        self.submenu = administrationPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("Merchant")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Merchant is ok.")

        self.form = MerchantPage(self.driver, self.help)

    def actionsModifyMerchantData(self):

        errorclickTabProcessingData = self.form.clickTabProcessingData()

        if len(errorclickTabProcessingData) != 0:
            self.error.append(errorclickTabProcessingData)



        time.sleep(2)



       # errorClicTabMerchantData = self.form.clickTabMerchantData()
       ## if len(errorClicTabMerchantData) != 0:
       #     self.error.append(errorClicTabMerchantData)
       # time.sleep(2)
