import time
from ddt import data, ddt
# from ExternalPages.emailConditions import EmailConditions
# from Conditions.GeneralConditions.LoginGeneralConditions import loginGC
# from ExternalPages.getPasswordFromEmailActions import EmailActions4
from Conditions.loginConditions import LoginConditions
from PagesObject.Actions.loginActions import LoginActions
from PagesObject.Actions.menuActions import MenuActions
from PagesObject.Actions.Administration.rolesActions import rolesActions
from PagesObject.Actions.Administration.merchantParametersActions import merchantParametersActions
from PagesObject.Actions.Administration.merchantActions import merchantActions
from PagesObject.Actions.Administration.usersActions import usersActions
from PagesObject.Actions.Cards.saleActions import saleActions
from ExternalPages.getPasswordFromEmailActions import EmailActions
from Tests.test_login_2 import getPasswordMailinator

# from ExternalPages.test_getPasswordFromEmail import TestGetPasswordFromEmail

@ddt
class Test0001(LoginConditions):
    page = "login test Page"

    '''
    def test_0001(self):
        self.name_test = "Log in to the application successfully"
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(2)

    def test_0002(self):
        self.name_test = "Log in to the application successfully providing a username containing valid special characters."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('specialChar')
        time.sleep(2)

    
    def test_0003(self):
        self.name_test = "Log in to the application successfully after changing an already expired password."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('changeExpiredPwd')
        time.sleep(2)

    
    def test_0004(self):
        self.name_test = "Attempt to log in to the application providing invalid credentials."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('invalid')
        time.sleep(2)

    
    def test_0005(self):
        self.name_test = "Attempt to log in to the application when the user is blocked."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('blocked')
        time.sleep(2)

    
    def test_0006(self):
        self.name_test = "Attempt to log in to the application providing an invalid Merchant ID."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('invalidMerchant')
        time.sleep(2)

    
    def test_0007(self):
        self.name_test = "Reset password successfully."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsResetPassword('standard')

        self.driver.get(self.help.get_parameters()["url_email"])
        time.sleep(3)
        actionEmail = EmailActions(self.driver, self.help)
        password = actionEmail.actionsGo('standard')
        time.sleep(3)
        self.driver.get(self.help.get_parameters()["url"])
        self.driver.refresh()
        time.sleep(3)
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLoginNewPassword('standard',password,'Cenpos@45','Cenpos@45')
        time.sleep(4)

    def test_0017(self):
        self.name_test = "Validate that the application is honoring the user role permissions by only displaying menu options for the ones the user has the corresponding privilege."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = rolesActions(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsDeleteRol()
            actionRoles.actionsNewRol('optMenutest')

        time.sleep(2)

    def test_0023(self):
        self.name_test = "Successfully create a new user."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = rolesActions(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsDeleteRol()
            actionRoles.actionsNewRol('optMenutest')
            
        time.sleep(5)

    def test_0018(self):
        self.name_test = "Successfully update/modify an already existing user role."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = rolesActions(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsEditRol()

        time.sleep(5)


    def test_0021(self):
        self.name_test = "Permanently delete an already existing user role."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = rolesActions(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
            actionRoles.actionsDeleteRol()
        else:
            actionRoles.actionsDeleteRol()

        time.sleep(2)


    def test_0023(self):
        self.name_test = "Successfully create a new user."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = usersActions(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if not result:
            actionUsers.actionsNewUser('optMenutest')

        time.sleep(5)

    def test_0008(self):
        self.name_test = "Cancel the password change prompt after receiving the temporary password."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsResetPassword('standard')
        self.driver.get(self.help.get_parameters()["url_email"])

        actionEmail = EmailActions(self.driver, self.help)
        password = actionEmail.actionsGo('standard')

        self.driver.get(self.help.get_parameters()["url"])
        self.driver.refresh()

        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLoginNewPasswordCancel('standard',password)

    def test_0009(self):
        self.name_test = "Attempt to reset the password when trying to set a new password that does not meet the history requirements."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsResetPassword('standard')
        self.driver.get(self.help.get_parameters()["url_email"])
        time.sleep(3)
        actionEmail = EmailActions(self.driver, self.help)
        password = actionEmail.actionsGo('standard')
        time.sleep(3)
        self.driver.get(self.help.get_parameters()["url"])
        self.driver.refresh()
        time.sleep(3)
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLoginNewPassword('standard',password, self.help.get_parameters()["passwords"]['standard'], self.help.get_parameters()["passwords"]['standard'])
        time.sleep(4)

    def test_0010(self): 
        self.name_test = "Attempt to reset the password by entering different values into the 'New Password' and 'Confirm Password' fields."

        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsResetPassword('standard')
        self.driver.get(self.help.get_parameters()["url_email"])
        time.sleep(3)
        actionEmail = EmailActions(self.driver, self.help)
        password = actionEmail.actionsGo('standard')
        time.sleep(3)
        self.driver.get(self.help.get_parameters()["url"])
        self.driver.refresh()
        time.sleep(3)
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLoginNewPassword('standard',password,'Cenpos@45','Cenpos@46')
        time.sleep(4)
    

    def test_0007(self):
        self.name_test = "Successfully log out of the application."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(1)
        actionLogout = DeshboardActions(self.driver, self.help)
        actionLogout.actionsLogout()
        time.sleep(2)

    
    def test_0012(self):
        self.name_test = "Successfully change password from the top user menu in the application."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(2)
        DeshboardActions.actionsChangePasswordFromTopUser(self,'Cenpos@2022','Cenpos@2022')
        time.sleep(3)

   
    def test_0013(self):
        self.name_test = "Attempt to change password from the top user menu in the application when trying to set a new password that does not meet the history requirements."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(2)
        DeshboardActions.actionsChangePasswordFromTopUser(self,self.help.get_parameters()["passwords"]['standard'],self.help.get_parameters()["passwords"]['standard'])
        time.sleep(3)
    
    def test_0014(self):
        self.name_test = "Attempt to change password from the top user menu in the application when entering different values into the New Password and Confirm Password fields."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(2)
        DeshboardActions.actionsChangePasswordFromTopUser(self, self.help.get_parameters()["passwords"]['standard'], self.help.get_parameters()["passwords"]['standard']+"")
        time.sleep(3)
    
    def test_0015(self):
        self.name_test = "Successfully switch to and from linked merchant accounts."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        DeshboardActions.actionsSwitchMerchant(self)
        time.sleep(5)

    def test_0016(self):
        self.name_test = "Special characters validation."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        time.sleep(2)
     
    def test_0033(self):
        self.name_test = "Successfully update/modify current merchant settings."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        
        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Merchant")

        actions = merchantActions(self.driver, self.help)
        actions.actionsModifyMerchantData()


    @data("visa")
    def test_0055(self, value):
        self.name_test = "Successfully process a manual entry transaction when CVV is set to Required in the user role settings."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = rolesActions(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsEditRol_CVVSet("Required")

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = saleActions(self.driver, self.help, card=value)
        actionSale.fillform()

        time.sleep(5)
    '''

    @data("visa")
    def test_0068(self, value):
        self.name_test = "	Successfully process a declined transaction.."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = saleActions(self.driver, self.help, card=value)
        actionSale.fillformdecline()

        time.sleep(5)

    '''
    @data("visa")
    def test_0055B(self, value):
        self.name_test = "Successfully process a manual entry transaction when CVV is set to Must Pass Over in the user role settings."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Roles")

        actionRoles = rolesActions(self.driver, self.help)
        result = actionRoles.actionsSearchRol("optMenutest")

        if not result:
            actionRoles.actionsNewRol('optMenutest')
        else:
            actionRoles.actionsEditRol_CVVSet("Must Pass Over")

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = saleActions(self.driver, self.help, card=value)
        actionSale.fillform()

        time.sleep(5)

    
    def test_0034(self):
        self.name_test = "Successfully update/modify current merchant parameters settings."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')
        
        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "MerchantParameters")

        actions = merchantParametersActions(self.driver, self.help)

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
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Cards", "Sale")

        actionSale = saleActions(self.driver, self.help, card=value)
        actionSale.fillform()

        time.sleep(5)


    def test_0026(self):
        self.name_test = "Successfully update/modify an already existing user."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = usersActions(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if result:
            actionUsers.actionsUpdateUser()
        else:
            print("User not exist")
        time.sleep(2)


    def test_0027(self):
        self.name_test = "Permanently delete an already existing user."
        actionLogin = LoginActions(self.driver, self.help)
        actionLogin.actionsLogin('standard')

        actionSubmenu = MenuActions(self.driver, self.help)
        actionSubmenu.actionsMenu("Administration", "Users")

        actionUsers = usersActions(self.driver, self.help)
        result = actionUsers.actionsSearchUsers("optMenutest")

        if result:
            actionUsers.actionsDeleteUser()
        else:
            print("User not exist")
        time.sleep(2)

    
    '''
