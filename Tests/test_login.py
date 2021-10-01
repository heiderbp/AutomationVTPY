import time
from ddt import ddt

from Conditions.loginConditions import LoginConditions
from PagesObject.loginPage import LoginPage
from PagesObject.menuPage import MenuP
from PagesObject.headerPage import HeaderP
from PagesObject.Administration.rolesPage import RolesPage
from PagesObject.Administration.usersPage import UsersPage
from ExternalPages.getPasswordFromEmailActions import EmailActions
from PagesObject.Administration.merchantPage import MerchantPage
from PagesObject.Cards.salePage import SalePage
from PagesObject.Cards.manageTokenPage import ManageTokenPage
from PagesObject.Cards.useTokenPage import UseTokenPage
from PagesObject.Administration.merchantParametersPage import MerchantParametersPage

@ddt
class Test0001(LoginConditions):
    page = "login test Page"

    '''
    def test_0001(self):
        self.name_test = "Log in to the application successfully"
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

    def test_0002(self):
        self.name_test = "Log in to the application successfully providing a username containing valid special characters."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('specialChar')
    
    def test_0003(self):
        self.name_test = "Log in to the application successfully after changing an already expired password."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('changeExpiredPwd')
    
    def test_0004(self):
        self.name_test = "Attempt to log in to the application providing invalid credentials."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('invalid')
    
    def test_0005(self):
        self.name_test = "Attempt to log in to the application when the user is blocked."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('blocked')

    def test_0006(self):
        self.name_test = "Attempt to log in to the application providing an invalid Merchant ID."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('invalidMerchant')
    
    def test_0007(self):
        self.name_test = "Reset password successfully."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsResetPassword('standard')

        self.driver.get(self.help.get_parameters()["url_email"])

        actionEmail = EmailActions(self.driver, self.help)
        password = actionEmail.actionsGo('standard')

        self.driver.get(self.help.get_parameters()["url"])
        self.driver.refresh()

        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLoginNewPassword('standard',password,'Cenpos@45','Cenpos@45')


    def test_0017(self):
        self.name_test = "Validate that the application is honoring the user role permissions by only displaying menu options for the ones the user has the corresponding privilege."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsDeleteRol()
            actionRoles.actionsNewRol('optMenutest')

    def test_0023(self):
        self.name_test = "Successfully create a new user."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsDeleteRol()
            actionRoles.actionsNewRol('optMenutest')

    def test_0018(self):
        self.name_test = "Successfully update/modify an already existing user role."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsEditRol()

        time.sleep(5)
'''

    def test_0021(self):
        self.name_test = "Permanently delete an already existing user role."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
            actionRoles.actionsDeleteRol()
        else:
            actionRoles.actionsDeleteRol()

'''
    def test_0023(self):
        self.name_test = "Successfully create a new user."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if not result:
            actionUsers.actionsNewUser('optMenutest')

        time.sleep(5)

    def test_0008(self):
        self.name_test = "Cancel the password change prompt after receiving the temporary password."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsResetPassword('standard')
        self.driver.get(self.help.get_parameters()["url_email"])

        actionEmail = EmailActions(self.driver, self.help)
        password = actionEmail.actionsGo('standard')

        self.driver.get(self.help.get_parameters()["url"])
        self.driver.refresh()

        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLoginNewPasswordCancel('standard',password)

    def test_0009(self):
        self.name_test = "Attempt to reset the password when trying to set a new password that does not meet the history requirements."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsResetPassword('standard')
        self.driver.get(self.help.get_parameters()["url_email"])
        time.sleep(3)
        actionEmail = EmailActions(self.driver, self.help)
        password = actionEmail.actionsGo('standard')
        time.sleep(3)
        self.driver.get(self.help.get_parameters()["url"])
        self.driver.refresh()
        time.sleep(3)
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLoginNewPassword('standard',password, self.help.get_parameters()["passwords"]['standard'], self.help.get_parameters()["passwords"]['standard'])
        time.sleep(4)

    def test_0010(self): 
        self.name_test = "Attempt to reset the password by entering different values into the 'New Password' and 'Confirm Password' fields."

        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsResetPassword('standard')
        self.driver.get(self.help.get_parameters()["url_email"])
        time.sleep(3)
        actionEmail = EmailActions(self.driver, self.help)
        password = actionEmail.actionsGo('standard')
        time.sleep(3)
        self.driver.get(self.help.get_parameters()["url"])
        self.driver.refresh()
        time.sleep(3)
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLoginNewPassword('standard',password,'Cenpos@45','Cenpos@46')
        time.sleep(4)
    

    def test_0007(self):
        self.name_test = "Successfully log out of the application."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        actionLogout = HeaderP(self.driver, self.help)
        actionLogout.actionsLogout()

    def test_0012(self):
        self.name_test = "Successfully change password from the top user menu in the application."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        HeaderP.actionsChangePasswordFromTopUser(self,'Cenpos@2022','Cenpos@2022')

    def test_0013(self):
        self.name_test = "Attempt to change password from the top user menu in the application when trying to set a new password that does not meet the history requirements."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        HeaderP.actionsChangePasswordFromTopUser(self,self.help.get_parameters()["passwords"]['standard'],self.help.get_parameters()["passwords"]['standard'])
    
    def test_0014(self):
        self.name_test = "Attempt to change password from the top user menu in the application when entering different values into the New Password and Confirm Password fields."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(2)
        HeaderP.actionsChangePasswordFromTopUser(self, self.help.get_parameters()["passwords"]['standard'], self.help.get_parameters()["passwords"]['standard']+"")
        time.sleep(3)
    
    def test_0015(self):
        self.name_test = "Successfully switch to and from linked merchant accounts."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        HeaderP.actionsSwitchMerchant(self)
        time.sleep(5)

    def test_0016(self):
        self.name_test = "Special characters validation."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(2)
     
    def test_0033(self):
        self.name_test = "Successfully update/modify current merchant settings."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        
        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Merchant")

        actions = MerchantPage(self.driver, self.help)
        actions.actionsModifyMerchantData()

    @data("visa")
    def test_0055(self, value):
        self.name_test = "Successfully process a manual entry transaction when CVV is set to Required in the user role settings."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsEditRol_CVVSet("Required")

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()

        time.sleep(5)
    
    @data("visa")
    def test_0068(self, value):
        self.name_test = "	Successfully process a declined transaction.."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillformdecline()

        time.sleep(5)        

    @data("visa")
    def test_0082(self, value):
        self.name_test = "Successfully process a tokenized transaction when CVV is set to Required/Optional/Must Pass Over in the user role settings."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "ManageToken")

        actionManageToken = ManageTokenPage(self.driver, self.help, card=value)
        actionManageToken.createNewCardToken()
        actionManageToken.fillform()

        self.token = actionManageToken.getToken()

        actionSubmenu.actionsMenu("Cards", "UseToken")

        actionUseToken = UseTokenPage(self.driver, self.help)
        actionUseToken.actionsUseToken(self.token)

        time.sleep(5)

    @data("visa")
    def test_0079(self, value):
        self.name_test = "Attempt to process a transactions that does not meet one or more of the AVS, ZIP and CVV merchant parameters."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsEditRol_CVV_AVS_ZIP_Set("Must Pass Over")

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "MerchantParameters")

        actions = MerchantParametersPage(self.driver, self.help)
        actions.actionsModifyMerchantParametersAvsZipCvv("false")

        actions.saveform()

        self.driver.refresh()

        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()
        time.sleep(15)
    
    @data("visa")
    def test_0073(self, value):
        self.name_test = "Successfully process a transaction providing an email with a custom (and valid) top level domain."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Merchant")

        actions = MerchantPage(self.driver, self.help)
        actions.actionsModifyMerchantDataSetEmail()

        self.driver.refresh()
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()
        time.sleep(15)
    
    @data("visa")
    def test_0085(self, value):
        self.name_test = "Successfully create a brand new card token."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "ManageToken")

        actionManageToken = ManageTokenPage(self.driver, self.help, card=value)
        actionManageToken.createNewCardToken()
        actionManageToken.fillform()

        time.sleep(5)


     @data("visa")
    def test_0080(self, value):
        self.name_test = "Attempt to process a transactions that does not meet one or more of the merchant risk parameters."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillformdecline()

        time.sleep(5)
    
    @data("visa")
    def test_0055B(self, value):
        self.name_test = "Successfully process a manual entry transaction when CVV is set to Must Pass Over in the user role settings."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsEditRol_CVVSet("Must Pass Over")

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()

        time.sleep(5)

    
    def test_0034(self):
        self.name_test = "Successfully update/modify current merchant parameters settings."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        
        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "MerchantParameters")

        actions = MerchantParametersPage(self.driver, self.help)

        actions.actionsModifyMerchantParametersAvs()
        self.help.info_log(self.page, self.name_test + " AVS")
        actions.actionsModifyMerchantParametersZip()
        self.help.info_log(self.page, self.name_test + " ZIP")
        actions.actionsModifyMerchantParametersCvv()
        self.help.info_log(self.page, self.name_test + " CVV")
        actions.saveform()
        self.help.info_log(self.page, self.name_test + " SAVE")
        time.sleep(5)
        
    @data("visa","commercial")
    def test_0053(self, value):
        self.name_test = "Successfully process a transaction."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()

        time.sleep(5)


    def test_0026(self):
        self.name_test = "Successfully update/modify an already existing user."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if result:
            actionUsers.actionsUpdateUser()
        else:
            print("User not exist")
        time.sleep(2)


    def test_0027(self):
        self.name_test = "Permanently delete an already existing user."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if result:
            actionUsers.actionsDeleteUser()
        else:
            print("User not exist")
'''