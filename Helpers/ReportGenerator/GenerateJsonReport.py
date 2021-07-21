import Helpers.Helps


class GenerateJson:

    # Constructor
    def __init__(self):
        self.page = 'Generator Json'

        self.helps = Helpers.Helps.Helps()

        self.routes = self.helps.open_file('Configurations/routes.json')
        self.config = self.helps.open_file(self.routes['json_files']['json_config'])

        self.old_data = self.helps.open_file(self.routes['json_files']['json_report'])

    # Get the json data
    def get_data(self, mid, env, id_test, test, trans, card, browser, result, reason):
        data = [{
            "Application": self.config['app']['name'],
            "Mid": mid,
            "Environment": env,
            "Id": id_test,
            "Tests": test,
            "Transaction": trans,
            "CardType": card,
            "Browser": browser,
            "Result": result,
            "Reason": reason
        }]
        # Create the new data
        new_data = self.old_data + data
        return new_data

    # Save the data in the json
    def save_data(self, mid, env, id_test, test, trans, card, browser, result, reason):
        data = self.get_data(mid, env, id_test, test, trans, card, browser, result, reason)
        self.helps.write_file(self.routes['json_files']['json_report'], data)

    # Clear the data in the json file
    def clear_data(self):
        data = list()
        self.helps.write_file(self.routes['json_files']['json_report'], data)
        self.helps.info_log(self.page, 'The data was clear')
