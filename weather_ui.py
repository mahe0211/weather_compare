import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class WeatherUi:
    def __init__(self, logger):
        self.logger = logger
        self.driver = webdriver.Chrome('C:\\Users\\mahes\\Downloads\\chromedriver')
        self.url = 'https://weather.com/'
        self.temp = dict()

    def get_weather_details(self, cities):
        self.logger.info('Starting to get weather details from web url {}'.format(self.url))
        try:
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            for ct in cities:
                WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH,
                                                                                 "//input[@id='LocationSearch_input']"
                                                                                 ))).click()
                search_elem = self.driver.find_element_by_id('LocationSearch_input')
                search_elem.clear()
                search_elem.send_keys(ct)
                WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located((By.ID,
                                                                                            "LocationSearch_listbox")))
                time.sleep(5)
                search_elem.send_keys(Keys.RETURN)
                temp_elem = self.driver.find_element_by_xpath('//span[@data-testid="TemperatureValue"]')
                temperature = temp_elem.text[:-1]
                self.temp[ct] = temperature

            self.logger.info(self.temp)
            return self.temp

        except Exception:
            self.logger.error('Failed to access web url')
            raise Exception("Failed to access web url")
        finally:
            self.logger.info('Going to close browser')
            self.driver.quit()
