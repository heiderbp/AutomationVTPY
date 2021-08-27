import time
from ExternalPages.getPasswordFromEmailPage import EmailPage


class EmailActions:
    def __init__(self, driver, helps):
        self.driver = driver
        self.help = helps
        self.error = list()
        self.page = "Email Page"

    def actionsGo(self, user):

            go = EmailPage(self.driver, self.help)
            fill = go.write_user(user)

            if(len(fill)!=0):
                self.error.append(fill)

            write = go.click_go()
            if (len(write) != 0):
                self.error.append(write)

            time.sleep(4)

            write = go.click_first_element()
            if (len(write) != 0):
                self.error.append(write)

            time.sleep(2)

            password = go.get_password_from_email()

            return password

