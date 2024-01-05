import yaml
class OptionsReader:
    cities: list

    def __init__(self):
        cities = []

    @staticmethod
    def getCities():
        with open('cities.yaml') as file:
            cities = yaml.load(file, Loader=yaml.FullLoader)
            return cities

