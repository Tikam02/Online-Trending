from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://127.0.0.1:8000")

eleUserMessage = driver.find_element_by_link_text("FAQ").click()

time.sleep(2)
