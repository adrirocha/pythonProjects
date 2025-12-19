from dotenv import load_dotenv
import os
import tweepy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10

load_dotenv()

TWITTER_API_KEY  = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.long_wait = WebDriverWait(self.driver, timeout=120)
        self.short_wait = WebDriverWait(self.driver, timeout=7)

        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        sleep(5)
        try:
            accept_btn = self.short_wait.until(ec.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
            accept_btn.click()
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        self.long_wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a')))
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        self.driver.quit()

    def tweet_at_provider(self):
        if (PROMISED_DOWN > self.down) or (PROMISED_UP > self.up):
            message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            client = tweepy.Client(TWITTER_BEARER_TOKEN, TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
            client.create_tweet(text=message)

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
