from DataFactory.LoginData import LoginData
from PageObjects.LoginPO import LoginPO
from Tests.BaseTest import BaseTest
from Utilities.configuration_manager import ConfigurationManager
from Utilities.SeleniumHelper import SeleniumHelpers

class test_LoginTests(BaseTest):
    loginData = LoginData().login_data()
    config = ConfigurationManager().base_url()

    def setUp(self):
        self.driver = super().setup()
        self.login = LoginPO(self.driver)
        self.selenium = SeleniumHelpers(self.driver)

    def test_verify_the_user_can_login_successful(self):
        self.driver.get(self.config)
        self.login.fill_login_form(self.loginData)
        self.assertEqual(self.driver.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index","Url didn't match")
