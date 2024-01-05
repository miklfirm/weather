import weather_classes.OptionsReader
import weather_classes.config
import weather_classes.RequestSender
import weather_classes.DataWriter
from datetime import datetime
import pandas

API_KEY = '342bd634cd094b3eac0163643240501'
URL = f'http://api.weatherapi.com/v1/current.json'

# print(weather_classes.OptionsReader.OptionsReader.getCities())


cities = weather_classes.OptionsReader.OptionsReader.getCities()
# print(cities)
c_o = weather_classes.RequestSender.Connection()
info = dict()
for one_element in cities:
    info[str(one_element)] = str(c_o.getTemperature(one_element))

info["Date & time"] = str(datetime.now())

# print(info)
weather_classes.DataWriter.DataWriter.writeParams([info])
