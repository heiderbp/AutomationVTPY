import sys

import pdfkit

import Helpers.Helps


class Report:

    # Constructor
    def __init__(self):
        self.page = 'Generator Report'

        self.help = Helpers.Helps.Helps()

        routes = self.help.open_file('Configurations/routes.json')

        # Set the path of all json files
        path_to_json_data = './' + routes['json_files']['json_report']
        path_to_json_config = './' + routes['json_files']['json_config_options']
        name = self.help.open_file(routes['json_files']['json_config'])
        self.path_to_template = './' + routes['report_folders']['html_template']
        self.path_to_report = routes['report_folders']['report_folder']
        self.extension = '.pdf'
        self.app = name['app']['name'].replace(" ", "-") + "_"

        self.date = self.help.get_date()

        # Open the json files
        self.report_json = self.help.open_file(path_to_json_data)

        self.json_pdf_options = self.help.open_file(path_to_json_config)

    # Render the template with the data
    def template_rendering(self):
        template = "The data is empty"
        render_template = self.help.get_template(self.path_to_template)
        if len(self.report_json) != 0:
            datas = self.report_json
            date = self.date
            passed, failed, skipped = self.get_total_element()
            total = passed + failed + skipped
            template = render_template.render(datas=datas, date=date, passed=passed, failed=failed, skipped=skipped,
                                              total=total)

        return template

    # Generate the pdf file
    def generate_pdf(self):
        self.help.create_folder(self.path_to_report)

        date = self.help.get_date().replace(" ", '_')
        hour = self.help.get_hour().replace(":", '_')

        file_name = str(self.path_to_report + self.app + date + "_" + hour + self.extension)

        html = self.template_rendering()
        if html != 'The data is empty':
            if sys.platform == 'win32':
                path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
                config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
                pdfkit.from_string(html, file_name, options=self.json_pdf_options, configuration=config)
            elif sys.platform == 'linux':
                pdfkit.from_string(html, file_name, options=self.json_pdf_options)

            self.help.info_log(self.page, "The pdf report was generated")

    def get_total_element(self):
        length = len(self.report_json)
        passed = 0
        failed = 0
        skipped = 0
        item = 0
        while length > 0:
            if self.report_json[item]['Result'] == 'Passed':
                passed += 1
                item += 1
                length -= 1
            elif self.report_json[item]['Result'] == 'Failed':
                failed += 1
                item += 1
                length -= 1
            else:
                skipped += 1
                item += 1
                length -= 1
        return passed, failed, skipped
