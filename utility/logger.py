from loguru import logger
import datetime
import os

HOME_dir = os.getcwd()
logfilepath = os.path.join(HOME_dir, 'Logs')
os.makedirs(logfilepath, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(logfilepath, f"test_log_{timestamp}.log")

logger.add(log_file, rotation="1 week", retention="10 days", enqueue=True, backtrace=True, diagnose=True)
