import unittest

from Utilities.DriverManager import DriverManager


class BaseTest(unittest.TestCase):
    driver_manager = DriverManager()

    def setup(self):
        return self.driver_manager.setUp()

    def teardown(self):
        self.driver_manager.tearDown()

