import requests


class WeatherApi:

    def __init__(self, logger):
        self.logger = logger
        self.api = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={units}'
        self.key = 'c69dc1d42c7730b9290ec63e21b85e16'
        self.temp = dict()

    def get_weather_details(self, cities, units='metric'):
        for ct in cities:
            url = self.api.format(city=ct, key=self.key, units=units)
            #self.logger.info('api url to access weather details: {}'.format(url))
            try:
                resp = requests.get(url)
                self.logger.info('Status code for {} : {}'.format(ct, resp.status_code))
                try:
                    temperature = resp.json()['main']['temp']
                    self.temp[ct] = temperature
                except KeyError:
                    self.logger.error('No temperature data found for {}'.format(ct))
            except Exception:
                raise Exception('Failed to connect api end point')
        self.logger.info(self.temp)
        return self.temp
