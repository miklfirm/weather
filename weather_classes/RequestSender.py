import requests
API_KEY = '342bd634cd094b3eac0163643240501'
URL = f'http://api.weatherapi.com/v1/current.json'

class Connection:
    API_KEY: str
    URL: str
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
