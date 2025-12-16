from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, timeout=7)

driver.get("https://tinder.com")
driver.maximize_window()

driver.refresh()

sleep(3)
while True:
    try:
        deny_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/button')
        deny_button.click()
    except NoSuchElementException:
        pass
    else:
        break

while True:
    try:
        no_interest_popup_button = driver.find_element(By.XPATH, '//*[@id="u1121575413"]/div/div/div[2]/button[2]/div[2]/div[2]/div')
        no_interest_popup_button.click()
    except NoSuchElementException:
        pass
        
    deny_button.click()
# ----------------------------------------- First time + Login with Facebook -------------------------------------------------------------------
#accept_cookies = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="u-1445010807"]/div/div[2]/div/div/div[1]/div[1]/button')))
#accept_cookies.click()

#driver.find_element(By.XPATH, '//*[@id="u-1445010807"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/header/div/div[2]/div[2]/a').click()

#sleep(3)

#login_with_facebook = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="u1121575413"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')))
#login_with_facebook.click()

#base_window = driver.window_handles[0]
#fb_login_window = driver.window_handles[1]

#driver.switch_to.window(fb_login_window)
#print(driver.title)

#email_input = wait.until(ec.presence_of_element_located((By.NAME, "email")))
#email_input.send_keys(FACEBOOK_EMAIL)

#password_input = driver.find_element(By.NAME, "pass")
#password_input.send_keys(FACEBOOK_PASSWORD)
#password_input.send_keys(Keys.ENTER)

#continue_with_login = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[role='button'] span")))
#continue_with_login.click()

#driver.switch_to.window(base_window)
#print(driver.title)


