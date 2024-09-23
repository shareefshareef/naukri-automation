from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
import time

class ANaukri():

    def __init__(self,email="#type username or email",password="#type your password"):

        self.credentials = {
            'email' : email,
            'password' : password,
            'url' : 'https://www.naukri.com/nlogin/login'
        }

        self.browser = webdriver.Chrome()

    def login(self):
        try:
            self.browser.get(self.credentials['url'])
            username = self.browser.find_element(By.ID,"usernameField")
            username.clear()
            username.send_keys(self.credentials['email'])
            time.sleep(1)
            password = self.browser.find_element(By.ID,"passwordField")
            password.clear()
            password.send_keys(self.credentials['password'])

            try:
                submit = self.browser.find_element(By.XPATH,"//button[text() = 'Login']")
                submit.click()
            except Exception as e:
                print(f"Submit Error {e}")

            time.sleep(4)

        except Exception as e:
            print(f"An Error Occured at {e}")
            logging.error(e)


    def close(self):
        self.browser.quit()

    



