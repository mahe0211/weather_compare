from weather_ui import WeatherUi
from weather_api import WeatherApi
from datetime import datetime as dt
from config import data
import logging


class Comparator:
    def __init__(self, logger):
        self.logger = logger
        self.weather_ui = WeatherUi(logger)
        self.weather_api = WeatherApi(logger)
        self.result = dict()

    def get_temp_comparision(self, cities, variance):
        self.logger.info('Starting weather details comparision from UI and API')
        temp_from_ui = self.weather_ui.get_weather_details(cities)
        temp_from_api = self.weather_api.get_weather_details(cities)
        for ct in cities:
            res = abs(float(temp_from_ui.get(ct, 0)) - float(temp_from_api.get(ct, 0)))
            if res < variance:
                self.result[ct] = True
            else:
                self.result[ct] = False
        return self.result


if __name__ == '__main__':
    today = dt.today().strftime("%Y-%m-%d")
    fmt = '%(asctime)-8s %(process)-4s %(message)s'
    logging.basicConfig(filename='weather_compare_{}.log'.format(today), level='INFO', filemode='w', format=fmt)
    logger = logging.getLogger()
    cities = data['city']
    variance = data['variance']
    comp = Comparator(logger)
    result = comp.get_temp_comparision(cities, variance)
    logger.info("result {}".format(result))
    print(result)
