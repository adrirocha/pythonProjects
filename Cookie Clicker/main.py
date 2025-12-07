from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
sleep(3)

driver.find_element(By.ID, value="langSelect-EN").click()

try:
    cookie_consent = driver.find_element(By.CLASS_NAME, "cc_btn")
    cookie_consent.click()
except:
    print("Cookie banner not found.")

cookies_count = driver.find_element(By.ID, value="cookies")
count = 0
while True:
    driver.find_element(By.ID, value="bigCookie").click()
    count += 1
    if count % 50 == 0:
        upgrades = driver.find_elements(By.CLASS_NAME, value="unlocked")
        if upgrades:
            price_upgrade_dict = {}
            for upgrade in upgrades:
                upgrade_id = upgrade.get_attribute("id")
                try:
                    upgrade_text = upgrade.find_element(By.CLASS_NAME, "price").text
                    # Remove vírgulas se houver
                    upgrade_price = int(upgrade_text.replace(",", ""))
                    price_upgrade_dict[upgrade_price] = upgrade_id
                except ValueError:
                    continue

            current_cookies_text = driver.find_element(By.ID, value="cookies").text.split()[0]
            current_cookies = int(current_cookies_text.replace(",", ""))
            for price in sorted(list(price_upgrade_dict.keys()), reverse=True):
                if current_cookies >= price:
                    element_id = price_upgrade_dict[price]
                    driver.find_element(By.ID, value=element_id).click()
    if count >= 3000:
        cookies_per_second = driver.find_element(By.CSS_SELECTOR, value="#cookies #cookiesPerSecond").text.split()[-1]
        print(f"cookies/second : {cookies_per_second}")
        break
    
driver.quit()
        

        
