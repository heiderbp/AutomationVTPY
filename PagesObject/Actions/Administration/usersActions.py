import time

from PagesObject.Pages.administrationPage import administrationPage
from PagesObject.Pages.Administration.usersPage import UsersPage


class usersActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Users Actions Page"

        self.form = UsersPage(self.driver, self.help)

    def actionsClickSearch(self):

        errorClicUsersSearch = self.form.clickUsersSearch()
        if len(errorClicUsersSearch) != 0:
            self.error.append(errorClicUsersSearch)


    def actionsSearchUsers(self, text):

        self.form = UsersPage(self.driver, self.help)
        txtResultUser = self.form.getTxtResultUser()
        errorWriteUserSearch = self.form.writeUserSearch(text)
        print(txtResultUser)
        if txtResultUser == "No matching records found":
            result = False
        else:
            result = True
        if len(errorWriteUserSearch) != 0:
            self.error.append(errorWriteUserSearch)

        return result
    '''   while True:
            txtResultUser = self.form.getTxtResultUser()
            print(txtResultUser)
            if txtResultUser == 'Loading items...':
                time.sleep(1)
            else:
                break

    
        if txtResultUser == "No matching records found":
            result = False
        else:
            result = True
'''


    def actionsNewUser(self, text):
        self.form = UsersPage(self.driver, self.help)

        error = self.form.clickRowSelect()
        if len(error) != 0:
            self.error.append(error)

        time.sleep(1)

        error = self.form.fillform(text)
        if len(error) != 0:
            self.error.append(error)

        errorClicSave = self.form.clicksave()

        if len(errorClicSave) != 0:
            self.error.append(errorClicSave)

    def actionsDeleteUser(self):
        self.form = UsersPage(self.driver, self.help)

        error = self.form.clickRowDelete()
        if len(error) != 0:
            self.error.append(error)

        error = self.form.clickConfirmDeleteUser()
        if len(error) != 0:
            self.error.append(error)


    def actionsUpdateUser(self):
        self.form = UsersPage(self.driver, self.help)

        error = self.form.clickRowUpdate()
        if len(error) != 0:
            self.error.append(error)

        time.sleep(1)

        error = self.form.fillEditFieldsForm()
        if len(error) != 0:
            self.error.append(error)

        errorClicSave = self.form.clicksave()

        if len(errorClicSave) != 0:
            self.error.append(errorClicSave)

