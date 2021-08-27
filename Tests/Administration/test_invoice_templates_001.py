import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Administration.InvoiceTemplatesActions import invoiceTemplatesActions


class ClickInvoiceTemplates(dashBoardConditions):
    page = "Invoice Templates page"

    def test_ClickAllowed(self):
        self.name_test = "Click Combobox Sale"

        actions = invoiceTemplatesActions(self.driver, self.help)

        actions.actionsClickSale()
        self.help.info_log(self.page, self.name_test + " Search")

        time.sleep(5)
      #  self.error = actions.error