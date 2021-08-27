from ExternalPages.EmailGeneralConditions import emailGC


class EmailConditions(emailGC):

    def setUp(self) -> None:
        self.driver.refresh()

    def tearDown(self) -> None:
        self.help.tear_down(self.name_test, self.page, self.error,'mailinator')