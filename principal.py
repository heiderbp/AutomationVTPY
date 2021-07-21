from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
#import unittest
import time

###class vttest(unittest.TestCase):

def test_00001():           # Log in to the application successfully.
    driver = loaddriver()
    loginAdmin(driver)


   ## time.sleep(5)
   ## logout(driver)
    time.sleep(10)
def test_00002():           # Log in to the application successfully providing a username containing valid special characters.
    driver = loaddriver()
    loginUser(driver, '@ndresT3st', 'Cenpos@4', '30000720')
    time.sleep(10)
def test_00003():           # Log in to the application successfully after changing an already expired password.
    driver = loaddriver()
    loginUser(driver, 'PedroP', 'BMZZBJVL', '30000720')
    time.sleep(10)
    driver.find_element_by_id('newPassword').send_keys('Cenpos@3')
    driver.find_element_by_id('repeatNewPassword').send_keys('Cenpos@3')
    driver.find_element_by_id('changePassword').click()
    time.sleep(10)
def test_00004():           #Attempt to log in to the application providing invalid credentials.
    driver = loaddriver()
    driver.get('https://test.cenpos.net:7443/html5-apps/dev/spa-apps/app/vt/')
    driver.find_element_by_id('userName').send_keys('PedroTest2')
    driver.find_element_by_id('password').send_keys('BMZZBJVL')
    driver.find_element_by_id('merchant').send_keys('30000720')
    driver.find_element_by_id('submitLogin').click()
    time.sleep(10)
def test_00005():           #Attempt to log in to the application when the user is blocked.
    driver = loaddriver()
    driver.find_element_by_id('userName').send_keys('andreab')
    driver.find_element_by_id('password').send_keys('Cenpos@2')
    driver.find_element_by_id('merchant').send_keys('30000720')
    driver.find_element_by_id('submitLogin').click()
    time.sleep(10)
def test_00006():           #Attempt to log in to the application providing an invalid Merchan t ID.
    driver = loaddriver()
    driver.find_element_by_id('userName').send_keys('hbedoya')
    driver.find_element_by_id('password').send_keys('Cenpos@54')
    driver.find_element_by_id('merchant').send_keys('300007200')
    driver.find_element_by_id('submitLogin').click()
    time.sleep(10)
def test_00007():           #Reset password successfully.
    driver = loaddriver()
    driver.find_element_by_id('resetPassword').click()
    textMessage = driver.find_element_by_css_selector('#inspire>div.v-dialog__content.v-dialog__content--active>div>div>div.v-card__title').text

    if textMessage == 'Restore Password':
        driver.find_element_by_id('userRestore').send_keys('hbedoya')
        driver.find_element_by_id('merchantRestore').send_keys('hbedoya')
        driver.find_element_by_id('submitRestorePassword').click()
    else:
        print ('Error:' + textMessage + ', se esperaba title: Restore Password.')

    time.sleep(5)
def test_00008():           # Cancel the password change prompt after receiving the temporary password.
    print ('8')
def test_00009():           # Attempt to reset the password when trying to set a new password that does not meet the history requirements.
    print ('9')
def test_00010():           # Attempt to reset the password by entering different values into the "New Password" and "Confirm Password" fields.
    print ('10')
def test_00011():           # Successfully log out of the application.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00012():           #Successfully change password from the top user menu in the application.
    driver = loaddriver()
    loginUser(driver, 'george', 'Cenpos@2', '30000720')
    time.sleep(5)
    driver.find_element_by_css_selector('body>div>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large').click()
    time.sleep(5)
    driver.find_element_by_css_selector('body>div>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(1)').click()
    num = '2'
    driver.find_element_by_id('password').send_keys('Cenpos@' + num)
    driver.find_element_by_id('newPassword').send_keys("Cenpos@" + num)
    driver.find_element_by_id('repeatPassword').send_keys("Cenpos@" + num)
    driver.find_element_by_id('submitChangePassword').Click()
    time.sleep(10)
def test_00013():           #Attempt to change password from the top user menu in the application when trying to set a new password that does not meet the history requirements.
    driver = loaddriver()
    loginUser(driver, 'george', 'Cenpos@2', '30000720')
    time.sleep(5)
    driver.find_element_by_css_selector('body>div>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large').Click()
    driver.find_element_by_css_selector('body>div>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(1)').Click()
    time.sleep(5)
    driver.find_element_by_id('password').send_keys('Cenpos@' + num)
    driver.find_element_by_id('newPassword').send_keys("Cenpos@" + num)
    driver.find_element_by_id('repeatPassword').send_keys("Cenpos@" + num)
    driver.find_element_by_id('submitChangePassword').Click()
    time.sleep(10)
def test_00014():           #Attempt to change password from the top user menu in the application when entering different values into the "New Password" and "Confirm Password" fields.
    driver = loaddriver()
    loginUser(driver, 'george', 'Cenpos@2', '30000720')
    time.sleep(5)
    driver.find_element_by_css_selector('body>div>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large').click()
    time.sleep(5)
    driver.find_element_by_css_selector('body>div>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(1)').click()

    num = '2'
    driver.find_element_by_id('password').send_keys('Cenpos@' + num)
    driver.find_element_by_id('newPassword').send_keys("Cenpos@" + num)
    driver.find_element_by_id('repeatPassword').send_keys("Cenpos@3")
    driver.find_element_by_id('submitChangePassword').Click()

    time.sleep(10)
def test_00015():           #Successfully switch to and from linked merchant accounts.
    driver = loaddriver()
    loginAdmin(driver)
    time.sleep(10)
    driver.find_element_by_css_selector('#app>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large').click()
    driver.find_element_by_css_selector('#app>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(2)').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id=''app'']/div[4]/div/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]').click()
    driver.find_element_by_xpath('//*[@id=''app'']/div[4]/div/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]').click()
def test_00016():           #Special characters validation Sale.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00016A():           #Special characters validation Token..
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00016B():           # Special characters validation Sale.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00016C():           # Special characters validation Sale.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00016D():           # Special characters validation Sale.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00016E():           # Special characters validation Sale.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00016F():           # Special characters validation Sale.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00017():           # Validate that the application is honoring the user role permissions by only displaying menu options for the ones the user has the corresponding privilege.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00018():           # Successfully create a new user role.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00019():           # Attempt to create a new user role while leaving the "Role name" field empty.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00020():           # Successfully update/modify an already existing user role.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00021():           # Permanently delete an already existing user role.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00022():           # Select the "No" option when asked to permanently delete an existing user role.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00023():           # Successfully create a new user.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00023A():           # Attempt to create a new user that already exist.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00024():           # Attempt to create a new user while leaving one or more required fields empty.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00025():           # Successfully copy an existing user across a multimerchant linked group.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00026():           # Successfully update/modify an already existing user.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00027():           # Permanently delete an already existing user.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00028():           # Select the "No" option when asked to permanently delete an existing user
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00029():           # Successfully unlock an already existing user.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def test_00030():           # Successfully change password for an already existing user.
    driver = loaddriver()
    loginAdmin(driver);
    time.sleep(5)
    logout(driver);
def getPasswordFromEmail(driver):
    driver = webdriver.Chrome('Webdrivers\chromedriver.exe')
    driver.get('https://www.mailinator.com/')
    driver.find_element_by_id('addOverlay').send_keys('george')
    driver.find_element_by_id('go-to-public').click()

    driver.find_element_by_css_selector('#inboxpane>div>div>div>table>tbody>tr:nth-child(1)>td:nth-child(3)').click()
    driver.switch_to_frame(driver.find_element_by_id('msg_body'))
    txtInfo = driver.find_element_by_css_selector('body>table>tbody>tr:nth-child(3)>td>p:nth-child(1)').text
    txtInfo = txtInfo[ len(txtInfo) - 8:len(txtInfo)]
    driver.switch_to_default_content()
    return txtInfo

def loginAdmin(driver):
    wait = WebDriverWait(driver, 10)
    username = wait.until(ec.visibility_of_element_located((By.ID, 'userName')))
    password = wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    merchant = wait.until(ec.visibility_of_element_located((By.ID, 'merchant')))
    username.send_keys('hbedoya')
    password.send_keys('Cenpos@5')
    merchant.send_keys('30000720')
    ''' driver.find_element_by_id('userName').send_keys('hbedoya')
    driver.find_element_by_id('password').send_keys('Cenpos@5')
    driver.find_element_by_id('merchant').send_keys('30000720') '''
    driver.find_element_by_id('submitLogin').click()
    return driver


def loginUser(driver, user, password, merchant):
    driver.find_element_by_id('userName').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('merchant').send_keys(merchant)
    driver.find_element_by_id('submitLogin').click()
    return driver

def logout(driver):
##    driver.find_element_by_css_selector('# app > div.v-application--wrap > header > div > button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large').click()

    driver.find_element_by_css_selector('#app>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large').click()
   ## driver.find_element_by_css_selector('#app>div.v-application--wrap>header>div>button.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--large').click()
   ## driver.find_element_by_css_selector('#app>div.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active>div>div:nth-child(3)').click()

def loaddriver():
    driver = webdriver.Chrome('Webdrivers\chromedriver.exe')
    driver.get('https://webtest.cenpos.net/spa/app/vt')
    return driver

##getPasswordFromEmail()

test_00001()

# txtInfo =
# driver.quit()


#if __name__ == '__main__':
#    unittest.main()



