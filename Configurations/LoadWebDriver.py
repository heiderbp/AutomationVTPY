import os
import sys

from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class LoadWebDriver:

    # Constructor
    def __init__(self, helps):
        self.driver = None

        self.help = helps
        self.routes = self.help.open_file('Configurations/routes.json')
        config = self.help.open_file(self.routes['json_files']['json_config'])

        self.page = 'Load Selenium'

        browser = config['browser']['name']
        self.headless = config['browser']['headless']

        if browser == 'Firefox':
            self.setup_firefox()
        elif browser == 'Chrome':
            self.setup_chrome()
        elif browser == 'Edge':
            self.setup_edge()
        else:
            self.setup_chrome()

    # Set firefox option
    def setup_firefox(self):
        # Set firefox webdriver
        try:
            firefox_options = Options()
            if self.headless == 'True':
                firefox_options.headless = True
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options,
                                            service_log_path=os.devnull)
            self.driver.set_window_size(1920, 1080)
            self.driver.maximize_window()
            self.help.info_log(self.page, "The geckodriver loaded")
        except Exception as e:
            self.help.error_log(self.page, "The geckodriver failed: " + str(e))

    def setup_chrome(self):
        # Set chrome webdriver
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")

            if self.headless:
                chrome_options.add_argument("--headless")

            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            print(self.driver.get_window_size())
            self.driver.set_window_size(1920, 1080)
            print(self.driver.get_window_size())
            self.driver.maximize_window()
            print(self.driver.get_window_size())
            self.help.info_log(self.page, "The chromedriver loaded")
        except Exception as e:
            self.help.error_log(self.page, "The chromedriver failed: " + str(e))

    def setup_edge(self):
        # Set edge chromium webdriver
        try:
            if sys.platform == 'win32':
                options = EdgeOptions()
                options.use_chromium = True
                if self.headless == 'True':
                    options.add_argument("headless")
                options.add_argument("--start-maximized")
                self.driver = Edge(EdgeChromiumDriverManager().install())
                self.driver.maximize_window()
            else:
                options = EdgeOptions()
                options.binary_location = r'/usr/bin/microsoft-edge-dev'
                options.use_chromium = True
                if self.headless == 'True':
                    options.add_argument("headless")
                options.add_argument("--start-maximized")
                options.set_capability("platform", "LINUX")
                self.driver = Edge(executable_path="Webdrivers/msedgedriver", options=options)

            self.driver.set_window_size(1920, 1080)
            self.driver.maximize_window()

            self.help.info_log(self.page, "The edge chromium webdriver loaded and the window was maximized")
        except Exception as e:
            self.help.error_log(self.page, f"The edge chromium webdriver failed: {str(e)}")
