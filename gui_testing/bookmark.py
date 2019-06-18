from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://127.0.0.1:8002")
eleUserMessage = driver.find_element_by_id("txtSearch")
eleUserMessage.send_keys("Paris")
eleUserMessage = driver.find_element_by_xpath('//button[@name="submit"]').click()
eleUserMessage = driver.find_element_by_link_text("Login").click()
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_username")
eleUserMessage.send_keys("ChiragPoddar")
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_password")
eleUserMessage.send_keys("sen1234@")
time.sleep(2)
eleUserMessage = driver.find_element_by_id("submit").click()
time.sleep(2)
eleUserMessage = driver.find_element_by_xpath('//span[@class="star glyphicon glyphicon-star-empty"]').click()
time.sleep(2)
eleUserMessage = driver.find_element_by_xpath('//i[@class="glyphicon glyphicon-user"]').click()
time.sleep(1)
eleUserMessage = driver.find_element_by_link_text("See Bookmarks").click()
time.sleep(3)

