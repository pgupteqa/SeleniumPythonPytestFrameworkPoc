import datetime
import os

import allure


def take_screenshot_on_failure(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join("reports", filename)
    driver.save_screenshot(filepath)

    # Attach screenshot to Allure
    with open(filepath, "rb") as f:
        allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.PNG)