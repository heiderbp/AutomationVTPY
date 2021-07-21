import os
import sys

import Helpers.Helps


class Screenshots:

    # Constructor
    def __init__(self, driver):
        self.help = Helpers.Helps.Helps()

        self.routes = self.help.open_file('Configurations/routes.json')

        self.path = self.routes['report_folders']['screenshots_folder']

        self.driver = driver

        self.page = "Screenshot Method"

        path = os.getcwd()
        if path == 'C:\Program Files (x86)\Jenkins\workspace\Test' or \
                path == 'C:\Program Files (x86)\Jenkins\workspace\Simple_Cashiering':
            self.url = self.routes['server']['url'] + self.routes['report_folders']['screenshots_folder']
        else:
            self.url = path + '/' + self.routes['report_folders']['screenshots_folder']

        if sys.platform == 'win32':
            self.url = self.url.replace("\\", "/")

    # Method to generate the screenshots
    def generate_screenshots(self, name):
        screen = list()
        screenshot = dict()

        name = name + "-" + self.help.get_date() + "-" + self.help.get_hour() + ".png"

        screen_name = name.replace(" ", "_").replace(":", "-")

        # Save the screenshots
        try:
            self.driver.save_screenshot(self.path + screen_name)
            self.help.info_log(self.page, "The screenshots was saved")
        except Exception as e:
            self.help.error_log(self.page, "Something failed to take the screenshot: " + str(e))

        screenshot['Screen'] = screen_name
        screenshot['Url'] = self.url + screen_name
        screen.append(screenshot)

        return screen
