from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import config


def run_database_check():
    """
    This function will test all the links available in the UC Merced database
    :return: None
    """
    # path using the command prompt for windows
    driver = webdriver.Chrome(config.PATH_CHROME_DRIVER)
    # starting at the main page "All A-Z Databases"
    driver.get("https://libguides.ucmerced.edu/az.php")
    # move to next page after one second after page loaded
    timeout = 1

    # select div element where all the nodes with links exists
    elements = driver.find_elements_by_css_selector("div.s-lg-az-result-title a")

    # iterate over the node with links and save links in a list
    links = [elem.get_attribute('href') for elem in elements]

    print("LOADING " + str(len(links)) + " links...")
    start_index = 0

    # iterate over list of links and load links in the page
    for index in range(start_index, len(links)):
        try:
            # loads links using driver
            driver.get(links[index])
        except WebDriverException as e:
            # print message if error while loading
            print(str(index) + " " + driver.title + ": " + e.msg)
        try:
            # timeout logic
            element_present = EC.presence_of_element_located((By.ID, 'main'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            continue
        finally:
            # print name of the page and success if loaded successfully
            print(str(index) + " " + driver.title + ": SUCCESSFUL LOAD")
    driver.quit()


if __name__ == '__main__':
    run_database_check()
