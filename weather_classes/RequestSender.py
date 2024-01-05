import requests
import sys
sys.path.append("..")
from config.global_config import *

class Connection:
    city: str

    def __init__(self):
        self.API_KEY = API_KEY
        self.city = ""
        self.URL = URL

    def getTemperature(self, city):
        URLKeys = self.URL + "?key="+self.API_KEY+"&q="+city
        r = requests.get(url=URLKeys)
        result = r.json()
        return result.get('current').get('temp_c')
