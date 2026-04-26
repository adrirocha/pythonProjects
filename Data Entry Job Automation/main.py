from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests as r
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = os.getenv("FORM_URL")
USER_AGENT = os.getenv("USER_AGENT")

headers = {
    "User-Agent": USER_AGENT
}

response = r.get(ZILLOW_URL, headers=headers)
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(response.text, 'html.parser')
properties_links = [property_link.get("href") for property_link in soup.find_all("a", class_="property-card-link")]
properties_prices = [re.sub(r'[^0-9$,]', '', property_price.get_text()) for property_price in soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")]
properties_addresses = [property_address.get_text().strip().replace('|', '') for property_address in soup.find_all("address")]

class FormOperator:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=10)
    
    def access_form(self):
        self.driver.get(FORM_URL)
        self.driver.maximize_window()
    
    def fill_and_send_form(self):
        for i in range(0, len(properties_links)):
            self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//div[contains(text(), "SF Renting Research")]')))

            address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(properties_addresses[i])

            price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(properties_prices[i])

            link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(properties_links[i])

            self.driver.find_element(By.XPATH, '//span[contains(text(), "Enviar")]').click()

            self.wait.until(ec.presence_of_element_located((By.XPATH, '//div[contains(text(), "Sua resposta foi registrada.")]')))
            self.driver.find_element(By.LINK_TEXT, 'Enviar outra resposta').click()


form_operator = FormOperator()
form_operator.access_form()
form_operator.fill_and_send_form()
