import time
from Conditions.menuConditions import dashBoardConditions
from PagesObject.Actions.Administration.merchantParametersActions import merchantParametersActions


class UpdateMerchantParam(dashBoardConditions):
    page = "Merchant Parameters test page"

    def test_UpdateMerchantParam(self):
        self.name_test = "Update/Modify Merchant Parameters"

        actions = merchantParametersActions(self.driver, self.help)

        actions.actionsModifyMerchantParametersAvs()
        self.help.info_log(self.page, self.name_test + " AVS")
        actions.actionsModifyMerchantParametersZip()
        self.help.info_log(self.page, self.name_test + " ZIP")
        actions.actionsModifyMerchantParametersCvv()
        self.help.info_log(self.page, self.name_test + " CVV")
        actions.saveform()
        self.help.info_log(self.page, self.name_test + " SAVE")
        time.sleep(5)
      #  self.error = actions.error
