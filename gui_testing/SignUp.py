"""__author__ = 'urmi and minali'

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class homeButton(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:8000', desired_capabilities=DesiredCapabilities.FIREFOX) 
        #self.driver = webdriver.Firefox()
        

    def test_homeButton(self):
        driver = webdriver.Remote(command_executor='http://127.0.0.1:8000', desired_capabilities=DesiredCapabilities.FIREFOX) 

        #driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8000")
        driver.find_element_by_class_name('button').click()
	#driver.find_element_by_class_name("Home").text

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://127.0.0.1:8000")
#assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title

#eleUserMessage.clear()
eleUserMessage = driver.find_element_by_link_text("Sign Up").click()
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_username")
eleUserMessage.send_keys("ChiragPoddar")
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_email")
eleUserMessage.send_keys("chiragpoddar@gmail.com")
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_password1")
eleUserMessage.send_keys("sen1234@")
time.sleep(2)
eleUserMessage = driver.find_element_by_id("id_password2")
eleUserMessage.send_keys("sen1234@")
time.sleep(2)
eleUserMessage = driver.find_element_by_xpath('//button[@id="submit"]').click()
time.sleep(2)   
eleUserMessage = driver.find_element_by_link_text("BBC Sport").click()
time.sleep(2)
#eleUserMessage = driver.find_element_by_id("search")
#eleUserMessage.send_keys("Test Python")
time.sleep(4)
driver.close()
