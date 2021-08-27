import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class getPasswordMailinator:
    driver = None
    name_test = str()
    page = str()
    error = str()

    def __init__(self, driver_local):
        self.driver = driver_local
        print("inicio test")
       ## self.driver = webdriver.Chrome(ChromeDriverManager().install())
       ## self.driver.get("https://www.mailinator.com/v3/")
       ## self.driver.maximize_window()

        self.driver.execute_script("window.open('https://www.mailinator.com/v3/')")

        self.wait = WebDriverWait(self.driver, 10)

        try:
            self.txtInbox = self.wait.until(ec.visibility_of_element_located((By.ID, "inbox_field")))
            self.txtInbox.send_keys("heiderbp")
        except Exception as e:
            print("TextBox Inbox: {}".format(str(e)))

        try:
            self.btnGo = self.wait.until(ec.visibility_of_element_located((By.ID, "go_inbox")))
            self.btnGo.click()
        except Exception as e:
            print("Button go: {}".format(str(e)))

        try:
            self.itemListInbox = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#inboxpane>div>div>div>table>tbody>tr>td:nth-child(3)")))
            self.itemListInbox.click()
        except Exception as e:
            print("Button Item List Inbox: {}".format(str(e)))

        self.driver.switch_to.frame(self.driver.find_element_by_id("msg_body"))

        try:
            self.msgInbox = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "body>table>tbody>tr:nth-child(3)>td>p:nth-child(1)")))
            txtInfo = self.msgInbox.text[-8:]
            print("Password Temp {}".txtInfo)
        except Exception as e:
            print("Button go: {}".format(str(e)))


        return txtInfo

       # time.sleep(5)


#test = getPasswordMailinator()
