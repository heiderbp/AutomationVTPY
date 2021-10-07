import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class UsersPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Users Page"
        self.num = 0

        self.error = list()
        #self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Administration', 'users')

        self.txtPassword = None
        self.txtRepeatPassword = None
        self.txtName = None
        self.txtDepartment = None
        self.txtEmail = None
        self.txtCellPhoneNumber = None
        self.cmbInvoiceItem = None
        self.cmbRoleItems = None
        self.cmbPrinterOption = None

        try:
            self.txtSearch = self.wait.until(ec.visibility_of_element_located((By.ID, elements['txtSearch']['id'])))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        try:
            self.txtRowSelect = self.wait.until(ec.visibility_of_element_located((By.ID, "rowSelect")))
        except Exception as e:
            error_name = "Could not get the Row Select Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        try:
            self.txtResultUser = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                   "#tableUsers>div.v-data-table__wrapper>table>tbody>tr>td")))  # "#tableUsers>div>table>tbody>tr>td")))
        except Exception as e:
            error_name = "Could not get the ResultUser text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        try:
            self.btnDeleteUser = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableUsers>div.v-data-table__wrapper>table>tbody>tr>td:nth-child(8)>div>button:nth-child(4)")))
        except Exception as e:
            error_name = "Could not get the Delete User Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        try:
            self.btnUpdateUser = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableUsers>div.v-data-table__wrapper>table>tbody>tr>td:nth-child(8)>div>button:nth-child(1)")))
        except Exception as e:
            error_name = "Could not get the Update User Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        try:
            self.btnUnlockUser = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableUsers>div>table>tbody>tr>td.text-xs-center.no-print>div>button:nth-child(6)")))
        except Exception as e:
            error_name = "Could not get the Unlock User Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        try:
            self.btnChangePasswordUser = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableUsers>div>table>tbody>tr>td.text-xs-center.no-print>div>button:nth-child(8)>span>i")))
        except Exception as e:
            error_name = "Could not get the Change Password User Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

    def clickUsersSearch(self):
        error = list()
        fill = dict()
        method = "User Search"
        error += self.help.click_button(self.page, self.txtSearch)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeUserSearch(self, text):
        error = list()
        fill = dict()
        method = "User Search"

        error += self.help.write_field_text(self.page, "Search Text Role", self.txtSearch, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def getTxtResultUser(self):

        text = self.help.get_text(self.page, self.txtResultUser)

        try:
            self.txtResultFirstRow = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableRoles>div>table>tbody>tr:nth-child(1)>td.text-xs-center.no-print")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        return text

    def clickRowDelete(self):
        error = list()
        fill = dict()
        method = "Delete User"

        error += self.help.click_button(self.page, self.btnDeleteUser)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Delete User clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickConfirmDeleteUser(self):
        error = list()
        fill = dict()
        method = "Confirm Delete User"

        try:
            self.alertMessage = self.wait.until(ec.visibility_of_element_located((By.ID, "deleteUser")))
        except Exception as e:
            error_name = "Could not get alert message text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.alertMessage)


        if len(error) == 0:
            self.help.info_log(self.page, "The Confirm Delete User is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickConfirmDeleteUserNot(self):
        error = list()
        fill = dict()
        method = "Confirm Delete User"

        try:
            self.confirmDeleteUserNot = self.wait.until(
                ec.visibility_of_element_located((By.ID, "closeConfirmDeleteUser")))
        except Exception as e:
            error_name = "Could not get alert message text: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.confirmDeleteUserNot)

        if len(error) == 0:
            self.help.info_log(self.page, "The close Confirm Delete User is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickRowSelect(self):
        error = list()
        fill = dict()
        method = "New User"

        error += self.help.click_button(self.page, self.txtRowSelect)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button New user is clicked correctly")

        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickUserGroupAdmin(self):
        error = list()
        fill = dict()
        method = "Click User Group Admin"

        try:
            self.btnUserGroupAdmin = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableUsers>div>table>tbody>tr>td:nth-child(8)>div>button:nth-child(10)")))
        except Exception as e:
            error_name = "Could not get the Update User Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        error += self.help.click_button(self.page, self.btnUserGroupAdmin)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Update is clicked correctly")

        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickListItemsFirstElement(self):
        error = list()
        fill = dict()
        method = "Click List Items First Element"

        try:
            self.listItemsFirstElement = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-dialog__content.v-dialog__content--active>div>div>div.v-card__text>div>div>div>div>table>tbody>tr>td:nth-child(2)>div>div>div>div")))
        except Exception as e:
            error_name = "Could not get the Update User Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        error += self.help.click_button(self.page, self.listItemsFirstElement)

        if len(error) == 0:
            self.help.info_log(self.page, "The List Items First Element is clicked correctly")

        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickCopyUserGroup(self):
        error = list()
        fill = dict()
        method = "Click Copy User Group"

        try:
            self.btnCopyUserGroup = self.wait.until(ec.visibility_of_element_located((By.ID, "copyUserGroup")))
        except Exception as e:
            error_name = "Could not get the Copy User Group Button: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        error += self.help.click_button(self.page, self.btnCopyUserGroup)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Copy User Group is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickRowUpdate(self):
        error = list()
        fill = dict()
        method = "Update User"

        error += self.help.click_button(self.page, self.btnUpdateUser)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Update is clicked correctly")

        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def fillFormChangePassword(self, password, ConfirmPassword):
        error = list()
        fill = dict()

        try:
            self.txtNewPassword = self.wait.until(ec.visibility_of_element_located((By.ID, "newPassword")))
        except Exception as e:
            error_name = "Could not get the name input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtCPRepeatPassword = self.wait.until(ec.visibility_of_element_located((By.ID, "repeatPassword")))
        except Exception as e:
            error_name = "Could not get the name input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnSubmit = self.wait.until(ec.visibility_of_element_located((By.ID, "submit")))
        except Exception as e:
            error_name = "Could not get the name input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        self.txtNewPassword.send_keys(password)
        self.txtCPRepeatPassword.send_keys(ConfirmPassword)

        error += self.help.click_button(self.page, self.btnSubmit)

        if len(error) == 0:
            self.help.info_log(self.page, "Get Elements is ok")

        return fill

    def clickChangePasswordUser(self):
        error = list()
        fill = dict()
        method = "Change Password User"

        error += self.help.click_button(self.page, self.btnChangePasswordUser)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Change Password User is clicked correctly")

        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickRowUnlock(self):
        error = list()
        fill = dict()
        method = "Unlock User"

        error += self.help.click_button(self.page, self.btnUnlockUser)

        if len(error) == 0:
            self.help.info_log(self.page, "The Button Unlock is clicked correctly")

        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def loadForm(self):
        error = list()
        fill = dict()

        try:
            self.txtName = self.wait.until(ec.visibility_of_element_located((By.ID, "name")))
        except Exception as e:
            error_name = "Could not get the name input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtDepartment = self.wait.until(ec.visibility_of_element_located((By.ID, "department")))
        except Exception as e:
            error_name = "Could not get the department input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtEmail = self.wait.until(ec.visibility_of_element_located((By.ID, "email")))
        except Exception as e:
            error_name = "Could not get the email input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtCellPhoneNumber = self.wait.until(ec.visibility_of_element_located((By.ID, "cellPhoneNumber")))
        except Exception as e:
            error_name = "Could not get the cellPhoneNumber input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbInvoiceItem = self.wait.until(ec.visibility_of_element_located((By.ID, "invoiceOption")))
        except Exception as e:
            error_name = "Could not get the Invoice Combo box: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbRoleItems = self.wait.until(ec.visibility_of_element_located((By.ID, "hierarchyRoleId")))
        except Exception as e:
            error_name = "Could not get the Role Combo box: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbPrinterOption = self.wait.until(ec.visibility_of_element_located((By.ID, "receiptType")))
        except Exception as e:
            error_name = "Could not get the Printer Option Combo box: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if len(error) == 0:
            self.help.info_log(self.page, "Get Elements is ok")

        return fill

    def fillform(self, text):
        error = list()
        fill = dict()
        method = "New User"

        try:
            self.txtUserId = self.wait.until(ec.visibility_of_element_located((By.ID, "userId")))
        except Exception as e:
            error_name = "Could not get the userId input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtPassword = self.wait.until(ec.visibility_of_element_located((By.ID, "password")))
        except Exception as e:
            error_name = "Could not get the password input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtRepeatPassword = self.wait.until(ec.visibility_of_element_located((By.ID, "repeatPassword")))
        except Exception as e:
            error_name = "Could not get the repeatPassword input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        self.loadForm()

        self.txtUserId.send_keys(text)
        self.txtPassword.send_keys("Cenpos@2")
        self.txtRepeatPassword.send_keys("Cenpos@2")
        self.txtName.send_keys("Andrea Bastidas")
        self.txtDepartment.send_keys("QA")
        self.txtEmail.send_keys("heiderbp@hotmail.com")
        self.txtCellPhoneNumber.send_keys("323232323232")
        self.cmbInvoiceItem.send_keys("Do Not")
        self.cmbInvoiceItem.send_keys(Keys.ENTER)
        self.cmbRoleItems.send_keys("CenPOS Admin")
        self.cmbRoleItems.send_keys(Keys.ENTER)
        self.cmbPrinterOption.send_keys("Receipts")
        self.cmbPrinterOption.send_keys(Keys.ENTER)

        if len(error) == 0:
            self.help.info_log(self.page, "Get Elements is ok")

        return fill

    def fillEditFieldsForm(self):
        error = list()
        fill = dict()
        method = "Edit User"
        self.loadForm()

        error += self.help.write_field_text(self.page, method, self.txtName, "Williams Walki")
        error += self.help.write_field_text(self.page, method, self.txtDepartment, "QAS")
        error += self.help.write_field_text(self.page, method, self.txtEmail, "heiderbp@hotmail.com")
        error += self.help.write_field_text(self.page, method, self.txtCellPhoneNumber, "898989898989")

        if len(error) == 0:
            self.help.info_log(self.page, "The edit User textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clicksave(self):
        error = list()
        fill = dict()
        method = "Roles Page Button Save"

        try:
            self.parametersSave = self.wait.until(ec.visibility_of_element_located((By.ID, "save")))
        except Exception as e:
            error_name = "Could not get the parameter save button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.parametersSave)

        if len(error) == 0:
            self.help.info_log(self.page, "The save button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def actionsClickSearch(self):

        error = self.clickUsersSearch()
        if len(error) != 0:
            self.error.append(error)

    def actionsSearchUsers(self, text):
        txtResultUser = self.getTxtResultUser()
        error = self.writeUserSearch(text)
        print(txtResultUser)
        if txtResultUser == "No matching records found":
            result = False
        else:
            result = True
        if len(error) != 0:
            self.error.append(error)

        return result

    def actionsSearchUsersById(self, text):
        txtResultUser = self.getTxtResultUser()
        error = self.writeUserSearch(text)
        method = "Page Users actionsSearchUsersById"

        try:
            self.txtResultUserAll = self.wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                                                           "#tableUsers>div.v-data-table__wrapper>table>tbody>tr")))  # "#tableUsers>div>table>tbody>tr>td")))
        except Exception as e:
            error_name = "Could not get the ResultUser text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

        print(len(self.txtResultUserAll))

        for a in range(1, len(self.txtResultUserAll)):
            UserId = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#tableUsers>div.v-data-table__wrapper>table>tbody>tr:nth-child(" + str(a) + ")>td:nth-child(2)")))
            if UserId.text == text:
                self.num=a
                break

        if self.num != 0:
            btnChangePasswordUserById = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableUsers>div.v-data-table__wrapper>table>tbody>tr:nth-child(" + str(a) + ")>td:nth-child(8)>div>button:nth-child(8)")))
            self.help.click_button(self.page, btnChangePasswordUserById)

        if txtResultUser == "No matching records found":
            result = False
        else:
            result = True
        if len(error) != 0:
            self.error.append(error)

        return result

    def actionsNewUser(self, text):
        self.clickRowSelect()
        self.fillform(text)
        self.clicksave()

    def actionsDeleteUser(self):
        self.clickRowDelete()
        self.clickConfirmDeleteUser()

    def actionsDeleteUserNot(self):
        self.clickRowDelete()
        self.clickConfirmDeleteUserNot()

    def actionsUpdateUser(self):
        self.clickRowUpdate()
        self.fillEditFieldsForm()
        self.clicksave()

    def actionUserGroupAdmin(self):
        self.clickUserGroupAdmin()
        self.clickListItemsFirstElement()
        self.clickCopyUserGroup()

    def actionsUnlockUser(self):
        self.clickRowUnlock()

    def actionsChangePasswordUser(self):
        self.clickChangePasswordUser()
        self.fillFormChangePassword("Cenpos@2", "Cenpos@2")

    def actionsChangePasswordUserDistinct(self):
        self.clickChangePasswordUser()
        self.fillFormChangePassword("Cenpos@2", "Cenpos@3")





