from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://127.0.0.1:8000")
action = ActionChains(driver);
last_height = driver.execute_script("return document.body.scrollHeight")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
eleUserMessage = driver.find_element_by_link_text("Feedback")
time.sleep(1)
action.move_to_element(eleUserMessage).perform()
time.sleep(1)
eleUserMessage.click()
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_name")
eleUserMessage.send_keys("Chirag")
time.sleep(1)
eleUserMessage = driver.find_element_by_id("id_email")
eleUserMessage.send_keys("chirag@gmail.com")
time.sleep(1)
eleUserMessage = driver.find_element_by_id("id_subject")
eleUserMessage.send_keys("Login is not working.")
time.sleep(1)
eleUserMessage = driver.find_element_by_id("id_message")
eleUserMessage.send_keys("I am unable to login depsite creating my account. Have a look at it and resolve it asap.")
time.sleep(1)
eleUserMessage = driver.find_element_by_xpath('//button[contains(text(),"Submit")]').click()
time.sleep(3)

