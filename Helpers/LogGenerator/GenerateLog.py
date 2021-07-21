import datetime
import json
import logging
import os


class Logs:

    def __init__(self):
        file = open('Configurations/routes.json', 'r')
        routes = json.load(file)
        file.close()

        file = open(routes['json_files']['json_config'], 'r')
        name = json.load(file)
        file.close()

        app_name = name['app']['name']

        self.date = datetime.datetime.now()

        folder_path = routes['report_folders']['logs_folder']
        self.create_folder(folder_path)
        file_name = folder_path + self.generate_name(app_name)
        logging.basicConfig(filename=file_name, format='%(asctime)s:\t   %(levelname)s:\t  %(message)s', filemode="a",
                            level=logging.INFO)

    def generate_name(self, app):
        name = app.replace(" ", "_")
        date = self.date.strftime("%x").replace("/", "-").replace(" ", "-")
        file_name = str(name) + '-' + date + '.log'
        return file_name

    @staticmethod
    def debug_log(message, extra):
        logging.debug(message+": %s", extra.replace("\n", ""))

    @staticmethod
    def info_log(message, extra):
        logging.info(message+": %s", extra.replace("\n", ""))

    @staticmethod
    def warning_log(message, extra):
        logging.warning(message+": %s", extra.replace("\n", ""))

    @staticmethod
    def error_log(message, extra):
        logging.error(message+": %s", extra.replace("\n", ""))

    @staticmethod
    def critical_log(message, extra):
        logging.critical(message+": %s", extra.replace("\n", ""))

    # Method to check if the folder exits or not
    @staticmethod
    def create_folder(path):
        # check if the folder exits
        if not os.path.isdir(path):
            os.mkdir(path)
