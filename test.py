from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import config


def run_test():
    # path using the command prompt for windows
    driver = webdriver.Chrome(config.PATH_CHROME_DRIVER)
    driver.get("https://libguides.ucmerced.edu/az.php")
    timeout = 1

    elements = driver.find_elements_by_css_selector("div.s-lg-az-result-title a")
    links = [elem.get_attribute('href') for elem in elements]
    print("LOADING " + str(len(links)) + " links...")
    start_index = 0
    for index in range(start_index, len(links)):
        try:
            driver.get(links[index])
        except WebDriverException as e:
            print(str(index) + " " + driver.title + ": " + e.msg)
        try:
            element_present = EC.presence_of_element_located((By.ID, 'main'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            continue
        finally:
            print(str(index) + " " + driver.title + ": SUCCESSFUL LOAD")
    driver.quit()


if __name__ == '__main__':
    run_test()
