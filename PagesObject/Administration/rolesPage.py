import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PagesObject.menuPage import MenuP

from PagesObject.administrationPage import administrationPage


class RolesPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Roles Page"

        self.error = list()
        self.wait = WebDriverWait(self.driver, 2)

        elements = self.help.get_element('Administration', 'roles')

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
            self.txtResultRol = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableRoles>div>table>tbody>tr>td")))

        except Exception as e:
            error_name = "Could not get the ResultRol text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            self.error.append(error_name)

    ###################
    ###################

    def actionsClickSearch(self):

        self.menu = MenuP(self.driver, self.help)
        errormenu = self.menu.clickbtnAdministration()
        if len(errormenu) != 0:
            self.error.append(errormenu)
        self.help.info_log(self.page, "Role Menu was loads correctly.")

        self.submenu = administrationPage(self.driver, self.help)
        self.errorsubmenu = self.submenu.clickSubmenu("Roles")
        if len(self.errorsubmenu) != 0:
            self.error.append(self.errorsubmenu)
        self.help.info_log(self.page, "Submenu Roles -> ok.")

        errorClicRoleSearch = self.clickRoleSearch()
        if len(errorClicRoleSearch) != 0:
            self.error.append(errorClicRoleSearch)
        time.sleep(2)

    def actionsSearchRol(self, text):

        errorWriteRoleSearch = self.writeRoleSearch(text)

        txtResultRol = self.getTxtResultRol()

        if txtResultRol == "No matching records found":
            result = False
        else:
            result = True

        if len(errorWriteRoleSearch) != 0:
            self.error.append(errorWriteRoleSearch)

        return result

    def actionsNewRol(self, text):
        self.clickRowSelect()
        self.writeRoleName(text)
        self.fillform()
        self.clicksave()

    def actionsDeleteRol(self):
        self.clickDeleteRol()

    def actionsDeleteRolNot(self):
        self.clickDeleteRolNot()

    def actionsEditRol(self):
        self.clickEditRol()
        self.click_random_check_debit_credit_card()
        self.clicksave()

    def actionsEditRol_CVVSet(self, option):
        self.clickEditRol()
        self.cmbCvvSelected(option)
        self.clicksave()

    def actionsEditRol_AVSSet(self, option):
        self.clickEditRol()
        self.cmbAvsSelected(option)
        self.clicksave()

    def actionsEditRol_ZIPSet(self, option):
        self.clickEditRol()
        self.cmbZipSelected(option)
        self.clicksave()

    def actionsEditRol_CVV_AVS_ZIP_Set(self, option):
        self.clickEditRol()
        self.cmbCvvSelected(option)
        self.cmbAvsSelected(option)
        self.cmbZipSelected(option)
        self.clicksave()

    def actionsEditRol_DisableKeyEntry_Set(self, option):
        self.clickEditRol()
        self.cmbDisableKeyEntrySelected(option)
        time.sleep(10)
        self.clicksave()

    ###################
    ###################

    def clickRoleSearch(self):
        error = list()
        fill = dict()
        method = "Role Search"
        error += self.help.click_button(self.page, self.txtSearch)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickEditRol(self):
        error = list()
        fill = dict()
        method = "Edit Role"

        try:
            self.btnEdit = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableRoles>div>table>tbody>tr:nth-child(1)>td.text-xs-center.no-print>div>button:nth-child(1)")))
        except Exception as e:
            error_name = "Could not get the Row Delete Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnEdit)

        if len(error) == 0:
            self.help.info_log(self.page, "The button delete is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def click_random_check_debit_credit_card(self):
        error = list()
        fill = dict()
        method = "Checkbox Rol Debit and Credit Card"

        for a in range(1, 29):
            num = random.randrange(1, 3)
            print("chek" + str(a) + " Si/no:" + str(num))
            if num == 1:
                checksDebitAndCreditCards = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div.v-card.v-sheet.theme--light>div.v-tabs.theme--light>div.v-window.v-item-group.theme--light.v-tabs-items>div>div>div>div>div:nth-child(2)>div>div.v-window.v-item-group.theme--light.v-tabs-items>div>div.v-window-item.v-window-item--active>div>div>div:nth-child(" + str(a) + ")>div>div>div.v-input__slot>div")))
                error += self.help.click_button(self.page, checksDebitAndCreditCards)
                if len(error) == 0:
                    self.help.info_log(self.page, "Checkbox (" + str(a) + ") is clicked correctly")
                else:
                    fill = self.help.make_error_list(self.driver, method, error)

        if len(error) == 0:
            self.help.info_log(self.page, "The checkbox Tab Debit and Credit Card is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickDeleteRol(self):
        error = list()
        fill = dict()
        method = "Delete Role"

        try:
            self.btnDelete = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableRoles>div>table>tbody>tr:nth-child(1)>td.text-xs-center.no-print>div>button:nth-child(4)>span>i")))
        except Exception as e:
            error_name = "Could not get the Row Delete Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnDelete)

        if len(error) == 0:
            self.help.info_log(self.page, "The button delete is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        try:
            self.btnConfirmDelete = self.wait.until(ec.visibility_of_element_located((By.ID, "deleteHierarchyRole")))
        except Exception as e:
            error_name = "Could not get the Confirm Delete Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnConfirmCancelDelete = self.wait.until(ec.visibility_of_element_located((By.ID, "showConfirmDeleteRole")))
        except Exception as e:
            error_name = "Could not get the Confirm Delete Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnConfirmDelete)

        if len(error) == 0:
            self.help.info_log(self.page, "The button confirm delete is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        try:
            self.MsgAlertApproved = self.wait.until(ec.element_to_be_clickable((By.ID, "closeAlert")))
        except Exception as e:
            error_name = "Could not get the close Alert Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.MsgAlertApproved)

        if len(error) == 0:
            self.help.info_log(self.page, "The button confirm delete is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickDeleteRolNot(self):
        error = list()
        fill = dict()
        method = "Delete Role Confirm Not"

        try:
            self.btnDelete = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableRoles>div>table>tbody>tr:nth-child(1)>td.text-xs-center.no-print>div>button:nth-child(4)>span>i")))
        except Exception as e:
            error_name = "Could not get the Row Delete Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnDelete)

        if len(error) == 0:
            self.help.info_log(self.page, "The button delete is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        try:
            self.btnConfirmCancelDelete = self.wait.until(ec.visibility_of_element_located((By.ID, "showConfirmDeleteRole")))
        except Exception as e:
            error_name = "Could not get the Confirm Delete Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.btnConfirmCancelDelete)

        if len(error) == 0:
            self.help.info_log(self.page, "The button Confirm Cancel Delete is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickRowSelect(self):
        error = list()
        fill = dict()
        method = "New Role"

        self.wait.until(ec.element_to_be_clickable((By.ID, "rowSelect")))

        error += self.help.click_button(self.page, self.txtRowSelect)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeRoleSearch(self, text):
        error = list()
        fill = dict()
        method = "Role Search"

        error += self.help.write_field_text(self.page, "Search Text Role", self.txtSearch, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The search textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeRoleName(self, text):
        error = list()
        fill = dict()
        method = "Role Name"

        try:
            self.txtRolName = self.wait.until(ec.visibility_of_element_located((By.ID, "rolName")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.write_field_text(self.page, "Name Text Role", self.txtRolName, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The name textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def getTxtResultRol(self):
        error = list()

        try:
            self.txtRowItem = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#tableRoles>div>table>tbody>tr>td.text-xs-center.no-print>div")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        text = self.help.get_text(self.page, self.txtResultRol)

        return text

    def fillform(self):
        error = list()
        fill = dict()

        try:
            self.cmbRol = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#app>div>main>div>div>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div>div>div:nth-of-type(2)>div")))
        except Exception as e:
            error_name = "Could not get the Combo box Rol item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        if len(error) == 0:
            self.help.info_log(self.page, "Get Elements is ok")

        return fill

    def cmbCvvSelected(self, option):
        error = list()
        fill = dict()
        method = "Edit Role"

        try:
            self.cmbCvv = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div>div>div.row.align-center.justify-center>div>div.v-card.v-sheet.theme--light>div.v-tabs.theme--light>div.v-window.v-item-group.theme--light.v-tabs-items>div>div>div>div>div:nth-child(1)>div:nth-child(2)>div:nth-child(3)>div>div>div:nth-child(2)>div>div>div.v-input__slot")))
        except Exception as e:
            error_name = "Could not get the Cvv ComoBox item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.cmbCvv)

        if len(error) == 0:
            self.help.info_log(self.page, "The cvv combo box is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        try:
            if option == "Do not prompt":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(1)")))
            elif option == "Optional":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(2)")))
            elif option == "Required":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(3)")))
            elif option == "Must Pass Over":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(4)")))

        except Exception as e:
            error_name = "Could not get the Avs " + option + " ComoBox item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.cmbOption)

        if len(error) == 0:
            self.help.info_log(self.page, "The cvv Option " + option + " from combo box is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def cmbAvsSelected(self, option):
        error = list()
        fill = dict()
        method = "Edit Role"

        try:
            self.cmbAvs = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div.v-card.v-sheet.theme--light>div.v-tabs.theme--light>div.v-window.v-item-group.theme--light.v-tabs-items>div>div>div>div>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div.v-input__slot")))
        except Exception as e:
            error_name = "Could not get the Avs ComoBox item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.cmbAvs)

        if len(error) == 0:
            self.help.info_log(self.page, "The avs combo box is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        try:
            if option == "Do not prompt":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(1)")))
            elif option == "Optional":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(2)")))
            elif option == "Required":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(3)")))
            elif option == "Must Pass Over":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(4)")))

        except Exception as e:
            error_name = "Could not get the Avs " + option + " ComoBox item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.cmbOption)

        if len(error) == 0:
            self.help.info_log(self.page, "The avs Option " + option + " from combo box is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def cmbZipSelected(self, option):
        error = list()
        fill = dict()
        method = "Edit Role"

        try:
            self.cmbZip = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div>div>div.row.align-center.justify-center>div>div.v-card.v-sheet.theme--light>div.v-tabs.theme--light>div.v-window.v-item-group.theme--light.v-tabs-items>div>div>div>div>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div>div>div:nth-child(2)>div>div>div.v-input__slot")))
        except Exception as e:
            error_name = "Could not get the Cvv ComoBox item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.cmbZip)

        if len(error) == 0:
            self.help.info_log(self.page, "The zip combo box is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        try:
            if option == "Do not prompt":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(1)")))
            elif option == "Optional":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(2)")))
            elif option == "Required":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(3)")))
            elif option == "Must Pass Over":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(4)")))

        except Exception as e:
            error_name = "Could not get the Avs " + option + " ComoBox item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.cmbOption)

        if len(error) == 0:
            self.help.info_log(self.page, "The Zip Option " + option + " from combo box is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def cmbDisableKeyEntrySelected(self, option):
        error = list()
        fill = dict()
        method = "Edit Role"

        try:
            self.cmbDisableKeyEntry = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div.container.custom-container.container--fluid>div>div.row.align-center.justify-center>div>div.v-card.v-sheet.theme--light>div.v-tabs.theme--light>div.v-window.v-item-group.theme--light.v-tabs-items>div>div>div>div>div:nth-child(1)>div:nth-child(2)>div:nth-child(4)>div>div>div:nth-child(2)>div>div>div.v-input__slot")))
        except Exception as e:
            error_name = "Could not get the Cvv ComoBox item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.cmbDisableKeyEntry)

        if len(error) == 0:
            self.help.info_log(self.page, "The zip combo box is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        try:
            if option == "Do not prompt":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(1)")))
            elif option == "Optional":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(2)")))
            elif option == "Required":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(3)")))
            elif option == "Must Pass Over":
                self.cmbOption = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(4)")))

        except Exception as e:
            error_name = "Could not get the Avs " + option + " ComoBox item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.cmbOption)

        if len(error) == 0:
            self.help.info_log(self.page, "The Zip Option " + option + " from combo box is clicked correctly")
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

        try:
            self.MsgAlertApproved = self.wait.until(ec.element_to_be_clickable((By.ID, "closeAlert")))
        except Exception as e:
            error_name = "Could not get the close Alert Button item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, self.MsgAlertApproved)

        if len(error) == 0:
            self.help.info_log(self.page, "The button confirm Create is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill
