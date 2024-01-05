from weather_classes.options_reader import OptionsReader
import weather_classes.RequestSender
import weather_classes.DataWriter
import sys
sys.path.append("..")
from config.global_config import *
from datetime import datetime


cities = OptionsReader.getCities()
# print(cities)
c_o = weather_classes.RequestSender.Connection()
info = dict()

for one_element in cities:
    info[str(one_element)] = str(c_o.getTemperature(one_element))

info["Date & time"] = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# print(info)
weather_classes.DataWriter.DataWriter.writeParams([info])
