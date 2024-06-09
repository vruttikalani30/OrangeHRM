from selenium import webdriver

from Utilities.configuration_manager import ConfigurationManager


# from selenium.webdriver.chrome.options import Options

class DriverManager:
    driver = None

    def __init__(self):
        self.configs = None

    def setUp(self) -> object:
        # option = Options()
        # option.add_argument("--headless")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        self.driver.close()
        self.driver.quit()




