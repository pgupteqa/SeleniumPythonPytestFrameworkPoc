import datetime
import json
import os
import sys


import pytest

## Used to remove warning messages after the test execution
sys.path.append( os.path.dirname(os.path.dirname( os.path.abspath( __file__ ) ) ) )

@pytest.mark.usefixtures("browser_setup", "log_on_failure")
class BaseTest:

    @staticmethod
    def get_data_from_json(path,keyname):
        with open(path) as f:
            test_data = json.load(f)
            test_list = test_data[keyname]
            return test_list

