# -*- coding: utf-8 -*-
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re

class LoginLogout(unittest.TestCase):

    def login(self, url, username, password):
        driver = self.driver
        print('\nConnecting ...')
        driver.get(url)
        driver.find_element(By.NAME,"username").send_keys(username)
        driver.find_element(By.NAME,"password").send_keys(password)
        driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
        print('\nConnected')
    
    # Fonction pour le processus de déconnexion
    def logout(self, driver):
        print('\nLogouting ...')
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
        print('\nLogouted')
        driver.implicitly_wait(5)
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test(self):
        driver = self.driver

        # Partie 1 - Login
        self.login("https://opensource-demo.orangehrmlive.com/", "Admin", "admin123")

        # # Partie 2 - Ajout Panier
        # driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        # driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
        # driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
        # driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']/a").click()

        # elements_du_panier = driver.find_elements(By.XPATH, "//div[@id='cart_contents_container']/div/div/div[@class='cart_item']")
        # assert len(elements_du_panier) == 3, "Le nombre d'éléments dans le panier n'est pas égal à 3"

        # # Partie 3 - Modification Panier
        # driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()

        # # Partie 4 - Validation de Panier
        # print(f'\n --------- In the cart are {len(elements_du_panier)} elements --------- \n')

        # # # add the elements to the cart
        # # driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        # # entre into the cart
        # driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']/a").click()
        # # click next-next-next
        # driver.find_element(By.ID,"checkout").click()
        # driver.find_element(By.ID, "first-name").clear()
        # driver.find_element(By.ID, "first-name").send_keys("first-name")
        # driver.find_element(By.ID, "last-name").clear()
        # driver.find_element(By.ID, "last-name").send_keys("last-name")
        # driver.find_element(By.ID, "postal-code").clear()
        # driver.find_element(By.ID, "postal-code").send_keys("postal-code")        
        # driver.find_element(By.ID,"continue").click()
        # driver.find_element(By.ID,"finish").click()
        # driver.find_element(By.ID,"back-to-products").click()
        # # entred into the cart
        # # driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']/a").click()
        # # check is the cart is empty
        # elements_du_panier = driver.find_elements(By.XPATH, "//div[@id='cart_contents_container']/div/div/div[@class='cart_item']")
        # # continue shopping
        # # driver.find_element(By.ID,"continue-shopping").click()
        # print(f'\n --------- In the cart are {len(elements_du_panier)} elements --------- \n')
        # assert len(elements_du_panier) == 0, "Dans le panier a reste qqch..."

        # Partie 5 - Logout
        self.logout(driver)
       
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
