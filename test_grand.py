# -*- coding: utf-8 -*-
# pip install selenium

from openai import OpenAI

import ai

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddVasia(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_grand_test(self):
        driver = self.driver

        # login
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.NAME,"username").send_keys("A")
        time.sleep(0.15)
        driver.find_element(By.NAME,"username").send_keys("d")
        time.sleep(0.15)
        driver.find_element(By.NAME,"username").send_keys("m")
        time.sleep(0.15)
        driver.find_element(By.NAME,"username").send_keys("i")
        time.sleep(0.15)
        driver.find_element(By.NAME,"username").send_keys("n")
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(0.5)
        driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()

        # add Vasia
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        time.sleep(1)
        # records count before add
        text = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span').text
        print(text)

        print('\n === AI === ')

        prompt = "Прочитай строку и ответом напиши число, которое ты встретил в этой строке. Только число."

        ai_reponse = ai.process_line_with_chatgpt(prompt, text)
        print(f'    {ai_reponse}')

        print(' === == === \n')

        records = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print(f'Total records before add : {len(records)}')

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")
        time.sleep(0.5)
        driver.find_element(By.NAME, "firstName").send_keys("Vasia")
        time.sleep(0.5)
        driver.find_element(By.NAME, "lastName").send_keys("surname")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").send_keys("vasia@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        # records count after add
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        records = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print(f'Total records after add : {len(records)}')

        # delete Vasia
        driver.implicitly_wait(10)

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        # records count before delete
        records = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print(f'Total records before delete : {len(records)}')

        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys("V")
        time.sleep(0.15)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys("a")
        time.sleep(0.15)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys("s")
        time.sleep(0.15)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys("i")
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys(Keys.DOWN)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[7]/div/button[2]/i").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        time.sleep(3)
        # records count after delete
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        records = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print(f'Total records after delete : {len(records)}')

        # logout
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
        time.sleep(2)
    
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
