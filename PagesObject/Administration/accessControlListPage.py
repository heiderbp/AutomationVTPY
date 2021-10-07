from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class AccessControlListPage:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.page = "Access Control List Page"

        error = list()
        self.error = dict()
        self.wait = WebDriverWait(self.driver, 5)
        elements = self.help.get_element('Administration', 'accessControlList')

        try:
            self.txtIpToAllowed = self.wait.until(ec.visibility_of_element_located((By.ID, 'ipToAllowed')))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtIpFromAllowed = self.wait.until(ec.visibility_of_element_located((By.ID, "ipFromAllowed")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnAddAllowedIp = self.wait.until(ec.visibility_of_element_located((By.ID, "addAllowedIp")))
        except Exception as e:
            error_name = "Could not get the Button add Allowed Ip: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnDeleteAllowedIp = self.wait.until(ec.visibility_of_element_located((By.ID, "deleteAllowedIp")))
        except Exception as e:
            error_name = "Could not get the Button add Allowed Ip: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbAllowedEnvironment = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div>div>div.row.align-center.justify-center>div>div.row>div:nth-child(1)>div:nth-child(2)>div.col-lg-4.col-12>div")))
        except Exception as e:
            error_name = "Could not get the ComboBox Environment: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.listItemAllowedIp = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div>main>div>div>div>div.row.align-center.justify-center>div>div.row>div:nth-child(1)>div:nth-child(3)>div>div>div>div>table>tbody>tr:nth-child(1)>td:nth-child(1)>div>div>div.v-input__slot>div>div")))
        except Exception as e:
            error_name = "Could not get the List item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        ################################
        ################################

        try:
            self.txtIpToDeny = self.wait.until(ec.visibility_of_element_located((By.ID, 'ipToDeny')))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.txtIpFromDeny = self.wait.until(ec.visibility_of_element_located((By.ID, "ipFromDeny")))
        except Exception as e:
            error_name = "Could not get the Search input text item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnAddDenyIp = self.wait.until(ec.visibility_of_element_located((By.ID, "addDenyIp")))
        except Exception as e:
            error_name = "Could not get the Button add Deny Ip: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.btnDeleteDenyIp = self.wait.until(ec.visibility_of_element_located((By.ID, "deleteDenyIp")))
        except Exception as e:
            error_name = "Could not get the Button add Deny Ip: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.cmbDenyEnvironment = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-application--wrap>main>div>div>div>div.row.align-center.justify-center>div>div.row>div:nth-child(2)>div:nth-child(2)>div.col-lg-4.col-12")))
        except Exception as e:
            error_name = "Could not get the ComboBox Environment: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        try:
            self.listItemDenyIp = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#app>div.v-application--wrap>main>div>div>div>div.row.align-center.justify-center>div>div.row>div:nth-child(2)>div:nth-child(3)>div>div>div>div>table>tbody>tr:nth-child(1)>td:nth-child(1)>div")))
        except Exception as e:
            error_name = "Could not get the List item: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)


    def clickTxtIpToAllowed(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.txtIpToAllowed)

        if len(error) == 0:
            self.help.info_log(self.page, "The IpToAllowed textbox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickCmbAllowedEnvironment(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.cmbAllowedEnvironment)

        if len(error) == 0:
            self.help.info_log(self.page, "The Environment ComboBox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickCmbAllowedEnvironmentItem(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        cmbAllowedEnvironmentItem = None

        try:
            cmbAllowedEnvironmentItem = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(2)")))
        except Exception as e:
            error_name = "Could not get the Item Environment: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, cmbAllowedEnvironmentItem)

        if len(error) == 0:
            self.help.info_log(self.page, "The Item Environment ComboBox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnAddAllowedIp(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.btnAddAllowedIp)

        if len(error) == 0:
            self.help.info_log(self.page, "The AddA Allowed Ip Button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnDeleteAllowedIp(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.btnDeleteAllowedIp)

        if len(error) == 0:
            self.help.info_log(self.page, "The Delete Allowed Ip Button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickListItemAllowedIp(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.listItemAllowedIp)

        if len(error) == 0:
            self.help.info_log(self.page, "The List Item Allowed Ip Button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtIpToAllowed(self, text):
        error = list()
        fill = dict()
        method = "Access Control List"

        error += self.help.write_field_text(self.page, "Ip To Allowed Text", self.txtIpToAllowed, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The Ip To Allowed textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtIpFromAllowed(self, text):
        error = list()
        fill = dict()
        method = "Access Control List"

        error += self.help.write_field_text(self.page, "Ip From Allowed Text", self.txtIpFromAllowed, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The Ip From Allowed textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    ##################################
    ##################################

    def clickCmbDenyEnvironment(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.cmbDenyEnvironment)

        if len(error) == 0:
            self.help.info_log(self.page, "The Environment ComboBox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickCmbDenyEnvironmentItem(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        cmbDenyEnvironmentItem = None

        try:
            cmbDenyEnvironmentItem = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                       "#app>div.v-menu__content.theme--light.menuable__content__active>div>div:nth-child(2)")))
        except Exception as e:
            error_name = "Could not get the Item Environment: {}".format(str(e))
            self.help.error_log(self.page, error_name)
            error.append(error_name)

        error += self.help.click_button(self.page, cmbDenyEnvironmentItem)

        if len(error) == 0:
            self.help.info_log(self.page, "The Item Environment ComboBox is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnAddDenyIp(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.btnAddDenyIp)

        if len(error) == 0:
            self.help.info_log(self.page, "The AddA Deny Ip Button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickBtnDeleteDenyIp(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.btnDeleteDenyIp)

        if len(error) == 0:
            self.help.info_log(self.page, "The Delete Deny Ip Button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def clickListItemDenyIp(self):
        error = list()
        fill = dict()
        method = "Access Control List"
        error += self.help.click_button(self.page, self.listItemDenyIp)

        if len(error) == 0:
            self.help.info_log(self.page, "The List Item Deny Ip Button is clicked correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtIpToDeny(self, text):
        error = list()
        fill = dict()
        method = "Access Control List"

        error += self.help.write_field_text(self.page, "Ip To Deny Text", self.txtIpToDeny, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The Ip To Deny textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    def writeTxtIpFromDeny(self, text):
        error = list()
        fill = dict()
        method = "Access Control List"

        error += self.help.write_field_text(self.page, "Ip From Deny Text", self.txtIpFromDeny, text)

        if len(error) == 0:
            self.help.info_log(self.page, "The Ip From Deny textbox is write correctly")
        else:
            fill = self.help.make_error_list(self.driver, method, error)

        return fill

    #######################################
    #######################################

    def actionAddNewAllowedIp(self):
        self.writeTxtIpToAllowed('190.184.15.175')
        self.clickBtnAddAllowedIp()

    def actionAddNewInvalidAllowedIp(self):
        self.writeTxtIpToAllowed('900.184.15.175')
        self.clickBtnAddAllowedIp()

    def actionDeleteAllowedIp(self):
        self.clickListItemAllowedIp()
        self.clickBtnDeleteAllowedIp()

    def actionAddNewRangeAllowedIp(self):
        self.writeTxtIpToAllowed('190.184.15.175')
        self.writeTxtIpFromAllowed('190.184.15.180')
        self.clickBtnAddAllowedIp()

    def actionAddNewInvalidRangeAllowedIp(self):
        self.writeTxtIpToAllowed('190.184.15.175')
        self.writeTxtIpFromAllowed('190.184.15.500')
        self.clickBtnAddAllowedIp()

    def actionAddNewRangeAllowedIpByEnvironment(self):
        self.writeTxtIpToAllowed('190.184.15.190')
        self.writeTxtIpFromAllowed('190.184.15.180')
        self.clickCmbAllowedEnvironment()
        self.clickCmbAllowedEnvironmentItem()
        self.clickBtnAddAllowedIp()

    def actionAddNewAllowedIpByEnvironment(self):
        self.writeTxtIpToAllowed('190.184.15.190')
        self.clickCmbAllowedEnvironment()
        self.clickCmbAllowedEnvironmentItem()
        self.clickBtnAddAllowedIp()

    #################################
    #################################

    def actionAddNewDenyIp(self):
        self.writeTxtIpToDeny('190.184.15.175')
        self.clickBtnAddDenyIp()

    def actionAddNewInvalidDenyIp(self):
        self.writeTxtIpToDeny('900.184.15.175')
        self.clickBtnAddDenyIp()

    def actionDeleteDenyIp(self):
        self.clickListItemDenyIp()
        self.clickBtnDeleteDenyIp()

    def actionAddNewRangeDenyIp(self):
        self.writeTxtIpToDeny('190.184.15.175')
        self.writeTxtIpFromDeny('190.184.15.180')
        self.clickBtnAddDenyIp()

    def actionAddNewInvalidRangeDenyIp(self):
        self.writeTxtIpToDeny('190.184.15.175')
        self.writeTxtIpFromDeny('190.184.15.500')
        self.clickBtnAddDenyIp()

    def actionAddNewRangeDenyIpByEnvironment(self):
        self.writeTxtIpToDeny('190.184.15.190')
        self.writeTxtIpFromDeny('190.184.15.200')
        self.clickCmbDenyEnvironment()
        self.clickCmbDenyEnvironmentItem()
        self.clickBtnAddDenyIp()

    def actionAddNewDenyIpByEnvironment(self):
        self.writeTxtIpToDeny('190.184.15.190')
        self.clickCmbDenyEnvironment()
        self.clickCmbDenyEnvironmentItem()
        self.clickBtnAddDenyIp()