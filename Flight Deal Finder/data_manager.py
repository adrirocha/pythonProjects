import requests
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:
    def __init__(self):
        self._headers = { "Authorization" : os.getenv("DATA_MANAGER_TOKEN") }      
        self._endpoint = os.getenv("DATA_MANAGER_ENDPOINT")
    
    def get_all_data(self):
        response = requests.get(url=self._endpoint, headers=self._headers)
        response.raise_for_status()

        all_data = response.json()
        return all_data["prices"]
    
    def update_iataCode(self, id, iataCode):
        body = {
            "price" : {
                "iataCode" : iataCode
                }
            }
        response = requests.put(url=f"{self._endpoint}{id}", json=body, headers=self._headers)
        response.raise_for_status()
