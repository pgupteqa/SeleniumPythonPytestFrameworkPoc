import datetime
import json
import os
import sys


import pytest

## Used to remove warning messages after the test execution
sys.path.append( os.path.dirname(os.path.dirname( os.path.abspath( __file__ ) ) ) )

@pytest.mark.usefixtures("log_on_failure")
class BaseTest:

    @pytest.fixture(autouse=True)
    def setup_driver(self, browser_setup):
        self.driver = browser_setup  # Only this assignment is needed

    @staticmethod
    def get_data_from_json(path,keyname):
        with open(path) as f:
            test_data = json.load(f)
            test_list = test_data[keyname]
            return test_list

