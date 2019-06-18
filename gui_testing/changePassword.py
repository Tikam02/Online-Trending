from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://127.0.0.1:8000")
action = ActionChains(driver);
eleUserMessage = driver.find_element_by_link_text("Login")
action.move_to_element(eleUserMessage).perform()
eleUserMessage.click()
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_username")
eleUserMessage.send_keys("ChiragPoddar")
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_password")
eleUserMessage.send_keys("chirag12")
time.sleep(2)
eleUserMessage = driver.find_element_by_id("submit").click()
time.sleep(2)
eleUserMessage = driver.find_element_by_xpath('//i[@class="glyphicon glyphicon-user"]').click()
time.sleep(2)
eleUserMessage = driver.find_element_by_link_text("Change Password").click()
time.sleep(3)
driver.find_element_by_id("id_old_password").send_keys("chirag12")
time.sleep(2)
driver.find_element_by_id("id_new_password1").send_keys("sen1234@")
time.sleep(2)
driver.find_element_by_id("id_new_password2").send_keys("sen1234@")
time.sleep(2)
driver.find_element_by_id("submit").click()
time.sleep(2)
