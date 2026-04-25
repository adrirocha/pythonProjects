from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from time import sleep

load_dotenv()
USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")
SIMILAR_ACCOUNT = "harukimurakami.author"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.long_wait = WebDriverWait(self.driver, timeout=60)
        self.short_wait = WebDriverWait(self.driver, timeout=10)
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        sleep(3)
        
        self.driver.find_element(By.XPATH, '//*[@id="_R_c9d9lplkldcpbn6b5ipamH1_"]').send_keys(USERNAME)
        self.driver.find_element(By.XPATH, '//*[@id="_R_cdd9lplkldcpbn6b5ipamH1_"]').send_keys(PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Entrar"]').click()

        try:
            deny_save_login = self.short_wait.until(ec.presence_of_element_located((By.XPATH, '//div[contains(text(), "Agora não")]')))
            deny_save_login.click()
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

        try:
            deny_enable_notification = self.short_wait.until(ec.presence_of_element_located((By.XPATH, '//button[contains(text(), "Agora não")]')))
            deny_enable_notification.click()
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        self.short_wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, f'a[href="/{SIMILAR_ACCOUNT}/followers/"]'))).click()
        self.short_wait.until(ec.presence_of_element_located((By.XPATH, '//div[contains(text(), "Seguidores")]')))
        modal_xpath = '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
        for _ in range(5):
            followers_popup = self.driver.find_element(By.XPATH, modal_xpath)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)   
            sleep(2)
    
    def follow(self):
        users_to_follow = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Seguir")]')
        for user_to_follow in users_to_follow:
            try:
                user_to_follow.click()
                sleep(1)
            except ElementClickInterceptedException:
                pass

instaFollower = InstaFollower()
instaFollower.login()
instaFollower.find_followers()
instaFollower.follow()
