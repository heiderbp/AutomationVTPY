import time
from ddt import ddt, data

from Conditions.loginConditions import LoginConditions
from PagesObject.loginPage import LoginPage
from PagesObject.menuPage import MenuP
from PagesObject.headerPage import HeaderP
from PagesObject.Administration.rolesPage import RolesPage
from PagesObject.Administration.usersPage import UsersPage
from ExternalPages.getPasswordFromEmailActions import EmailActions
from PagesObject.Administration.merchantPage import MerchantPage
from PagesObject.Cards.authPage import AuthPage
from PagesObject.Cards.salePage import SalePage
from PagesObject.Cards.manageTokenPage import ManageTokenPage
from PagesObject.Cards.useTokenPage import UseTokenPage
from PagesObject.Administration.merchantParametersPage import MerchantParametersPage
from PagesObject.Administration.accessControlListPage import AccessControlListPage
from PagesObject.Administration.countriesAclPage import CountriesACLPage
from PagesObject.Administration.invoiceTemplatesPage import InvoiceTemplatesPage

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

    def test_0011(self):
        self.name_test = "Successfully log out of the application."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        actionLogout = HeaderP(self.driver, self.help)
        actionLogout.actionsLogout()

    def test_0012(self):
        self.name_test = "Successfully change password from the top user menu in the application."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        action = HeaderP(self.driver, self.help)
        action.actionsChangePasswordFromTopUser('Cenpos@2022', 'Cenpos@2022')
        time.sleep(4)

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

        actionHeader = HeaderP(self.driver, self.help)
        actionHeader.actionsSwitchMerchant()
    
    def test_0016(self):
        self.name_test = "Special characters validation."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        
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

    def test_0018(self):
        self.name_test = "Successfully create a new user role."
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

    def test_0019(self):
        self.name_test = "Attempt to create a new user role while leaving the 'Role name' field empty."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('')
        else:
            actionRoles.actionsDeleteRol()
            actionRoles.actionsNewRol('')

    def test_0020(self):
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

    def test_0022(self):
        self.name_test = "Select the 'No' option when asked to permanently delete an existing user role."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
            actionRoles.actionsDeleteRolNot()
        else:
            actionRoles.actionsDeleteRolNot()

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

    def test_0024(self):
        self.name_test = "Attempt to create a new user while leaving one or more required fields empty."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if not result:
            actionUsers.actionsNewUser('')

    def test_0025(self):
        self.name_test = "Successfully copy an existing user across a multimerchant linked group."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if not result:
            actionUsers.actionsNewUser('optMenutest')
        else:
            actionUsers.actionUserGroupAdmin()

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

    def test_0028(self):
        self.name_test = "Select the 'No' option when asked to permanently delete an existing user."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if result:
            actionUsers.actionsDeleteUserNot()
        else:
            print("User not exist")

    def test_0029(self):
        self.name_test = "Successfully unlock an already existing user."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if result:
            actionUsers.clickRowUnlock()
        else:
            print("User not exist")

    def test_0030(self):
        self.name_test = "Successfully change password for an already existing user."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if result:
            actionUsers.actionsChangePasswordUser()
        else:
            print("User not exist")
  
    def test_0031(self):
        self.name_test = "Successfully change password for the current user (by selecting it from the user list)."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin("standard")

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        actionUsers.actionsSearchUsersById(self.help.get_parameters()["users"]["standard"])
        actionUsers.fillFormChangePassword("Elavon@2020", "Elavon@2020")

    def test_0032(self):
        self.name_test = "Attempt to change password for an already existing user when the 'New password' and 'Confirm password' fields do not match."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = UsersPage(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if result:
            actionUsers.actionsChangePasswordUserDistinct()
        else:
            print("User not exist")

    def test_0033(self):
        self.name_test = "Successfully update/modify current merchant settings."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        
        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Merchant")

        actions = MerchantPage(self.driver, self.help)
        actions.actionsModifyMerchantData()

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
        
    def test_0035(self):
        self.name_test = "Successfully add a new IP address to the 'Allowed IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewAllowedIp()
        
    def test_0036(self):
        self.name_test = "Successfully add a new IP address to the 'Allowed IP' section for an specific environment."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewAllowedIpByEnvironment()
        
    def test_0037(self):
        self.name_test = "Successfully add a new range of IP addresses to the 'Allowed IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewRangeAllowedIp()        

    def test_0038(self):
        self.name_test = "Successfully add a new range of IP addresses to the 'Allowed IP' section for an specific environment."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewRangeAllowedIpByEnvironment()
        
    def test_0039(self):
        self.name_test = "Permanently delete an IP address from the 'Allowed IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionDeleteAllowedIp()

    def test_0040(self):
        self.name_test = "Successfully add a new IP address to the 'Deny IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewDenyIp()

    def test_0041(self):
        self.name_test = "Successfully add a new IP address to the 'Deny IP' section for an specific environment."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewDenyIpByEnvironment()

    def test_0042(self):
        self.name_test = "Successfully add a new range of IP addresses to the 'Deny IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewRangeDenyIp()

    def test_0043(self):
        self.name_test = "Successfully add a new range of IP addresses to the 'Deny IP' section for an specific environment."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewRangeDenyIpByEnvironment()

    def test_0044(self):
        self.name_test = "Permanently delete an IP address from the 'Deny IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionDeleteDenyIp()

    def test_0045(self):
        self.name_test = "Attempt to add an invalid IP address to the 'Allowed IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewInvalidAllowedIp()

    def test_0046(self):
        self.name_test = "Attempt to add an invalid range of IP addresses to the 'Allowed IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewInvalidRangeAllowedIp()

    def test_0047(self):
        self.name_test = "Attempt to add an invalid IP address to the 'Denied IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewInvalidDenyIp()

    def test_0048(self):
        self.name_test = "Attempt to add an invalid range of IP addresses to the 'Denied IP' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "AccessControlList")

        actions = AccessControlListPage(self.driver, self.help)
        actions.actionAddNewInvalidRangeDenyIp()        

    def test_0049(self):
        self.name_test = "Successfully add a country to the 'Denied Country' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "CountriesAcl")

        actions = CountriesACLPage(self.driver, self.help)
        actions.actionDeniedCountry()

    def test_0050(self):
        self.name_test = "Successfully remove a country from the 'Denied Country' section."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "CountriesAcl")
        
        actions = CountriesACLPage(self.driver, self.help)
        actions.actionRemoveDeniedCountry()
    
    def test_0051(self):
        self.name_test = "Successfully set a custom invoice template for the desired transaction types."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "InvoiceTemplates")

        action = InvoiceTemplatesPage(self.driver, self.help)
        action.actionTemplateTransactionSetCustom()

    def test_0052(self):
        self.name_test = "Successfully set the default invoice template for a transaction type with a custom template set."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "InvoiceTemplates")

        action = InvoiceTemplatesPage(self.driver, self.help)
        action.actionTemplateTransactionSetDefault()
    '''

    @data("visa")
    def test_0053(self, value):
        self.name_test = "Successfully process a transaction."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()

    '''
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
        time.sleep(10)

    @data("visa")
    def test_0056(self, value):
        self.name_test = "Successfully process a manual entry transaction on a California based merchant."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('california')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform(userType='california')

        time.sleep(10)

    @data("commercial")
    def test_0066(self, value):
        self.name_test = "Successfully process a transaction using a commercial card."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()
        time.sleep(15)

    @data("visa")
    def test_0067(self, value):
        self.name_test = "Successfully process a transaction leaving optional fields empty in the application."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Merchant")

        actions = MerchantPage(self.driver, self.help)
        actions.clickTabProcessingData()
        actions.actionsModifyProcessingDataCmb("Customer Code", "Optional")

        self.driver.refresh()

        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()
        time.sleep(15)

    @data("visa")
    def test_0068(self, value):
        self.name_test = "	Successfully process a declined transaction.."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillformdecline()

    @data("visa")
    def test_0070(self, value):
        self.name_test = "Attempt to process a manual entry transaction when the DisableKeyEntry parameter is enabled in merchant settings."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = RolesPage(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        time.sleep(10)

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsEditRol_DisableKeyEntry_Set("Required")
        time.sleep(10)
        self.driver.refresh()

        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('optMenutest')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()

    @data("visa")
    def test_0073(self, value):
        self.name_test = "Successfully process a transaction providing an email with a custom (and valid) top level domain."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Merchant")

        actions = MerchantPage(self.driver, self.help)
        actions.actionsModifyProcessingDataCmb("Receipt Delivery", "Email")

        self.driver.refresh()
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()

    @data("invalid")
    def test_0075(self, value):
        self.name_test = "Attempt to process a transaction using an invalid card number."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()

        time.sleep(10)

    @data("visa", "mastercard")
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

    @data("visa")
    def test_0080(self, value):
        self.name_test = "Attempt to process a transactions that does not meet one or more of the merchant risk parameters."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillformdecline()

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

    @data("visa")
    def test_0069(self, value):
        self.name_test = "Successfully process a partially approved transaction."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Auth")

        action = AuthPage(self.driver, self.help, card=value)
        action.fillform()

    @data("visa")
    def test_0074(self, value):
        self.name_test = "Successfully process a transaction."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform(customEmail="myemailinvalid")
        time.sleep(6)

    @data("visa")
    def test_0081(self, value):
        self.name_test = "Attempt to process a transaction while one or more required fields are empty."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform(amount="")
        time.sleep(6)
    
    @data("visa")        
    def test_0078(self, value):
        self.name_test = "Attempt to process a transaction that falls within the "Dark Period" timeframe for declined transactions."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()
        time.sleep(6)

    @data("expired")
    def test_0053(self, value):
        self.name_test = "Attempt to process a transaction providing an expired credit card."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = SalePage(self.driver, self.help, card=value)
        actionSale.fillform()
        time.sleep(6)

    @data("visa")
    def test_0087(self, value):
        self.name_test = "Attempt to create a new card token providing information already used in existing tokens."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "ManageToken")

        actionManageToken = ManageTokenPage(self.driver, self.help, card=value)
        actionManageToken.createNewCardToken()
        actionManageToken.fillform()

        self.driver.refresh()

        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "ManageToken")

        actionManageToken = ManageTokenPage(self.driver, self.help, card=value)
        actionManageToken.createNewCardToken()
        time.sleep(5)
        actionManageToken.fillformCloneData()

        time.sleep(6)
        
    @data("visa")
    def test_0083(self, value):
        self.name_test = "Attempt to process a force transaction for an already forced authorization."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Auth")

        action = AuthPage(self.driver, self.help, card=value)
        action.fillform()
        
    @data("visa")
    def test_0084(self, value):
        self.name_test = "Successfully process a return for an original transaction with partial refunds previously processed."
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Auth")

        action = AuthPage(self.driver, self.help, card=value)
        action.fillform()
    
    @data("visa")
    def test_0086(self, value):
        self.name_test = "Successfully create a brand new card token when CVV is set to Required/Optional/Must Pass Over in the user role settings."
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
                
        self.driver.refresh()
        
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "ManageToken")

        actionManageToken = ManageTokenPage(self.driver, self.help, card=value)
        actionManageToken.createNewCardToken()
        actionManageToken.fillform()

        self.driver.refresh()
        
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
                
        self.driver.refresh()
        
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "ManageToken")

        actionManageToken = ManageTokenPage(self.driver, self.help, card=value)
        actionManageToken.createNewCardToken()
        actionManageToken.fillform()

        self.driver.refresh()
        
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
                
        self.driver.refresh()
        
        actionLogin = LoginPage(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuP(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "ManageToken")

        actionManageToken = ManageTokenPage(self.driver, self.help, card=value)
        actionManageToken.createNewCardToken()
        actionManageToken.fillform()

        self.driver.refresh()
        time.sleep(20)
'''