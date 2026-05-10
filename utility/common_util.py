import os
import time


def take_screenshot(driver):
    #folder name
    folder_path = "screenshots"
    #to create a folder
    os.makedirs(folder_path, exist_ok=True)
    #file name
    file_name = f"screenshot_{int(time.time())}.png"
    # concat file name and path
    file_path = os.path.join(folder_path, file_name)
    print(file_path)
    # take screenshot
    driver.save_screenshot(file_path)