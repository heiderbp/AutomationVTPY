import json
import random
import string
import unittest
from datetime import datetime

from chance import chance
from jinja2 import Environment, FileSystemLoader
from selenium.webdriver.common.keys import Keys

import Helpers.ReportGenerator.GenerateJsonReport
from Helpers.LogGenerator.GenerateLog import Logs
from Helpers.ScreenshotGenerator.GenerateScreenshots import Screenshots


class Helps(Logs):
    page = "Helps"
    tc = unittest.TestCase('__init__')

    def get_routes(self):
        return self.open_file('Configurations/routes.json')

    def get_parameters(self):
        return self.open_file(self.get_routes()['json_files']['json_parameters'])

    def get_card(self):
        return self.open_file(self.get_routes()['json_files']['json_card_file'])

    def get_elements(self):
        return self.open_file(self.get_routes()['json_files']['json_elements'])

    # Method to get the date
    @staticmethod
    def get_date():
        x = datetime.now().strftime("%a") + " " + datetime.now().strftime("%b") + " " + datetime.now().strftime("%d")\
            + " " + datetime.now().strftime("%Y")
        return x

    # Method to get the hour
    @staticmethod
    def get_hour():
        x = datetime.now().strftime("%X")
        return x

    @staticmethod
    def open_file(path) -> dict:
        file = open(path, 'r')
        files = json.load(file)
        file.close()
        return files

    @staticmethod
    def write_file(path, files) -> None:
        file = open(path, 'w')
        json.dump(files, file, indent=4)
        file.close()

    def write_field_text(self, page, field, element, text) -> list:
        error = list()
        try:
            er = self.clean_fields(page, field, element)
            if len(er) == 0:
                element.send_keys(text)
                self.info_log(page, "It was written in the {} text field.".format(field))
        except Exception as e:
            error_name = "Something went wrong cleaning and typing in the {} text field: {}".format(field, str(e))
            self.error_log(page, error_name)
            error.append(error_name)

        return error

    def clean_fields(self, page, field, element) -> list:
        error = list()
        try:
            if len(element.get_attribute("value")) != 0:
                element.send_keys(Keys.CONTROL + "a")
                element.send_keys(Keys.DELETE)
            self.info_log(page, "It was cleaned in the {} text field.".format(field))
        except Exception as e:
            error_name = "Something went wrong cleaning {} text field: {}".format(field, str(e))
            self.error_log(page, error_name)
            error.append(error_name)

        return error

    def click_button(self, page, element) -> list:
        error = list()

        try:
            element.click()
            self.info_log(page, "Clicked successfully.")
        except Exception as e:
            error_name = "Something failed to click in the button: {}".format(str(e))
            self.error_log(page, error_name)
            error.append(error_name)

        return error

    def check_data(self, page, check, data, expected) -> list:
        error = list()

        try:
            self.tc.assertEqual(data, expected)
            self.info_log(page, "The '{}' data was successfully verified, data: '{}', expected: '{}'".
                          format(check, data, expected))
        except Exception as e:
            error_name = "Something failed to check the {} data, data: '{}', expected: '{}' ({})".format(
                check, data, expected, str(e))
            self.error_log(page, error_name)
            error.append(error_name)

        return error

    def get_value(self, page, element) -> dict:
        error = list()
        value = dict()

        value["error"] = list()
        value["value"] = str()

        try:
            value["value"] = element.get_attribute("value")
            self.info_log(page, "The data was taken.")
        except Exception as e:
            error_name = "Something failed to get the value: {}".format(str(e))
            self.error_log(page, error_name)
            error.append(error_name)
            value["error"] = error

        return value

    def get_trx(self, trx=str()) -> dict:
        response = dict()
        response["error"] = []
        response["trx"] = str()
        error = list()

        try:
            response["trx"] = self.open_file(self.get_routes()['json_files']['trx'])[trx.lower()]
        except Exception as e:
            error_name = f"The transaction could not obtained: {str(e)}"
            self.error_log(self.page, error_name)
            error.append(error_name)
        response["error"] = error

        return response

    # Get the html template
    @staticmethod
    def get_template(path):
        env = Environment(loader=FileSystemLoader(path))
        template = env.get_template("template.html")
        return template

    @staticmethod
    def invoice_generate(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def get_expired_date() -> list:
        expired = list()

        c_month = int(datetime.now().strftime("%m"))
        c_year = int(datetime.now().strftime("%Y"))

        month = random.randint(1, 12)
        year = random.randint(c_year, 2034)

        if year == c_year:
            if month == 12:
                year += 1
            elif month == c_month:
                pass
            elif month < c_month:
                month += (c_month - month)

        if month <= 9:
            month = "{}{}".format("0", str(month))

        expired.append(str(month))
        expired.append(str(year))

        return expired

    @staticmethod
    def get_amount():
        amount = random.randint(1, 200)
        decimal = random.randint(1, 99)

        if amount <= 9:
            amount = "{}{}".format("0", str(amount))

        amount = float("{}.{}".format(amount, decimal))

        return str(amount)

    def generate_info(self):
        data = dict()
        expired = self.get_expired_date()

        data["amount"] = self.get_amount()
        data["month"] = expired[0]
        data["year"] = expired[1]
        data["name"] = str(chance.name())
        data["invoice"] = str(self.invoice_generate())
        data["email"] = str(chance.email())
        data["avs"] = str(chance.street())
        data["zip"] = str(chance.string(pool="123456789", length=5))
        data["account"] = str(chance.string(pool="0123456789", minimum=13, maximum=13))
        data["check"] = str(chance.string(pool="123456789", minimum=2, maximum=3))
        data["loan"] = str(chance.string(pool="123456789", minimum=1, maximum=3))
        data["cell"] = str(chance.phone(formatted=False))

        return data

    @staticmethod
    def make_error_list(driver, method, errors) -> dict:
        error = dict()

        screen = Screenshots(driver)
        screenshot = screen.generate_screenshots(method)

        error['Method'] = method
        error['Errors'] = errors
        error['NumbersErrors'] = len(errors)
        error['Screenshot'] = screenshot

        return error

    # Tear down method
    def tear_down(self, method, page, error, mid, trans=str(), card=str(), skip=False):
        id_test = method.lower().replace("(", " ").replace(")", " ").replace("'", " ")\
                      .replace(",", " ").replace(" ", "_") + "_" + trans + "_" + card

        # Check if the test had an error or not
        if len(error) == 0:
            status = 'Passed'
            self.info_log(page, "The '" + method + "' test passed")
        elif skip:
            status = 'Skipped'
            self.warning_log(page, "The '" + method + "' test was skipped")
        else:
            status = 'Failed'
            self.error_log(page, "The '" + method + "' test failed")

        json_r = Helpers.ReportGenerator.GenerateJsonReport.GenerateJson()
        routes = self.open_file('Configurations/routes.json')
        config = self.open_file(routes['json_files']['json_config'])

        json_r.save_data(mid, config['url']['name'], id_test, method, trans.capitalize(), card,
                         config['browser']['name'], status, error)

        self.info_log(page, "The '" + method + "' test data was saved")

    # Get the url from json file
    def get_url(self):
        url = str()

        try:
            routes = self.open_file('Configurations/routes.json')
            parameters = self.open_file(routes['json_files']['json_parameters'])
            url = parameters['url']
            self.info_log(self.page, "The url has been taken, is: " + url)
        except Exception as e:
            self.error_log(self.page, "Something failed with the generation of the url: " + str(e))

        return url

    def get_element(self, module, page):
        element = str()

        try:
            routes = self.open_file('Configurations/routes.json')
            elements = self.open_file(routes['json_files']['json_elements'])
            element = elements[module][page]
            self.info_log(self.page, "The element has been taken, for " + module + " - " + page + " json file")
        except Exception as e:
            self.error_log(self.page, "Something failed with the generation of the element: " + str(e))

        return element
