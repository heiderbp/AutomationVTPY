import unittest

from Helpers.Helps import Helps
from Helpers.ReportGenerator.GenerateJsonReport import GenerateJson
from Helpers.ReportGenerator.GenerateReport import Report


class ReportGenerator(unittest.TestCase):

    @staticmethod
    def test_generate():
        # Generate the report
        report = Report()
        report.generate_pdf()

        # Clear the json file
        clr_json = GenerateJson()
        clr_json.clear_data()
