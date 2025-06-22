import os
import configparser

HOME_dir = os.getcwd()
configfilepath = os.path.join(HOME_dir, 'Configuration', 'config.ini')

config = configparser.ConfigParser()
config.read(configfilepath)

Login_test_data_path = os.path.join(HOME_dir, config.get('paths','login_testdata_path'))