import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver= webdriver.Chrome("D:\\PythonTest\\PythonTest\\venv\\chromeDriver.exe")
def testlunchURL():

    driver.set_page_load_timeout(60)
    driver.get("XXX")
    driver.maximize_window()
    WebDriverWait(driver,90).until(EC.presence_of_element_located((By.NAME,"username")))
    print("Login Page is displayed")
def testlogin():
    driver.find_element_by_name("username").send_keys("XXX")
    driver.find_element_by_name("password").send_keys("XXX")
    driver.find_element_by_xpath("//div[contains(text(),'Login')]").click()
    element = WebDriverWait(driver,90).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@src,'integrichain_logo_header')]")))
    print("Home Page Displayed")
testlunchURL()
testlogin()