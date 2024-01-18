# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_wrong(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        error = ""
        print(f'\n === ERROR : {len(error)} ===\n')

        driver.find_element(By.NAME,"username").send_keys("wq")
        driver.find_element(By.NAME,"password").send_keys("qwe")
        driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
        
        error = str(driver.find_element(By.CLASS_NAME, "oxd-alert"))
        print(f'\n === ERROR : {len(error)} ===\n')

        assert len(error) > 0, "There are no errors while wrong creds."

        if len(error) == 0:
            print('\n --- NO ERRORS ---\n')
            print(error)
            print(f'\n === ERROR : {len(error)} ===\n')
            driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()






    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
