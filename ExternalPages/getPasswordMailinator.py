import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class getPasswordMailinator:
    driver = None

    name_test = str()
    page = str()
    error = str()

    def __init__(self):
        print("inicio test")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.mailinator.com/v3/")

        time.sleep(5)
