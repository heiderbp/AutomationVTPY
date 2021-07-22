import time
from Conditions.dashboardConditions import dashBoardConditions
from PagesObject.Actions.Gift.inquiryActions import InquiryActions


class ClickGiftInquiryMerchant(dashBoardConditions):
    page = "Inquiry page"

    def test_ClickMerchant(self):
        self.name_test = "Click Combobox Merchant"
        actions = InquiryActions(self.driver, self.help)
        actions.actionsClickCmbMerchant()
        self.help.info_log(self.page, self.name_test + " Search")
        time.sleep(5)
