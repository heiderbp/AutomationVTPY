import time

from PagesObject.Pages.headerPage import HeaderP
from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.cardPage import cardPage
from PagesObject.Pages.checkPage import checkPage
from PagesObject.Pages.giftPage import giftPage
from PagesObject.Pages.reportsPage import reportsPage

class HeaderActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Header Actions Page"
        self.login = HeaderP(self.driver, self.help)
        self.errormenu = dict()

    def actionsChangePasswordFromTopUser(self, new_password, confirm_password):
        form1 = HeaderP(self.driver, self.help)

        ClicProfile = form1.clickbtnProfile()
        if (len(ClicProfile) != 0):
            self.error.append(ClicProfile)

        ClicResetPassword = form1.clickProfileResetPassword()
        if (len(ClicResetPassword) != 0):
            self.error.append(ClicResetPassword)

        writeOldPassword = form1.writeTxtOldPassword('standard')
        if (len(writeOldPassword) != 0):
            self.error.append(ClicResetPassword)

        writeNewPassword = form1.writeTxtNewPassword(new_password)
        if (len(writeNewPassword) != 0):
            self.error.append(writeNewPassword)

        writeConfirmPassword = form1.writeTxtConfirmPassword(confirm_password)
        if (len(writeConfirmPassword) != 0):
            self.error.append(writeConfirmPassword)

        clicSubmit = form1.clickProfileResetSubmit()
        if (len(clicSubmit) != 0):
            self.error.append(clicSubmit)

    def actionsSwitchMerchant(self):
        form1 = HeaderP(self.driver, self.help)

        ClicProfile = form1.clickbtnProfile()
        if (len(ClicProfile) != 0):
            self.error.append(ClicProfile)

        ClicMultiMerchant = form1.clickProfileMultiMerchant()
        if (len(ClicMultiMerchant) != 0):
            self.error.append(ClicMultiMerchant)

        time.sleep(2)

        ClicMultiMerchantElement = form1.clickMultiMerchantElement()
        if (len(ClicMultiMerchantElement) != 0):
            self.error.append(ClicMultiMerchantElement)

    def actionsLogout(self):
        form1 = HeaderP(self.driver, self.help)

        frmClicProfile = form1.clickbtnProfile()
        if (len(frmClicProfile) != 0):
            self.error.append(frmClicProfile)

        frmClicLogout = form1.clickbtnLogout()
        if (len(frmClicLogout) != 0):
            self.error.append(frmClicLogout)