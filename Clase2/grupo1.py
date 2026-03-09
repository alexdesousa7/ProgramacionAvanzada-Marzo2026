import requests
import logging

logging.basicConfig(level=logging.INFO)


class WeatherForecastClient:

    DEFAULT_LATITUDE = 40.0
    DEFAULT_LONGITUDE = -2.0
    DEFAULT_NUM_DAYS = 10

    def __init__(self, latitude=DEFAULT_LATITUDE, longitude=DEFAULT_LONGITUDE):
        self.base_url = "https://api.open-meteo.com/v1/forecast"
        self.params = {
            "latitude": latitude,
            "longitude": longitude,
            "timezone": "auto"
        }
        self.__check_cords__()

    def __check_cords__(self):
        if not isinstance(self.params["latitude"], float) or not isinstance(self.params["longitude"], float):
            logging.error("Latitude and longitude must be floats")
            self.params["latitude"] = self.DEFAULT_LATITUDE
            self.params["longitude"] = self.DEFAULT_LONGITUDE
        if self.params["latitude"] < -90 or self.params["latitude"] > 90:
            logging.error("Latitude must be between -90 and 90")
            self.params["latitude"] = self.DEFAULT_LATITUDE
        if self.params["longitude"] < -180 or self.params["longitude"] > 180:
            logging.error("Longitude must be between -180 and 180")
            self.params["longitude"] = self.DEFAULT_LONGITUDE

    def get_forecast(self, params):
        res = requests.get(self.base_url, params=self.params)
        return res.json()


    def get_wind_forecast(self, num_days=DEFAULT_NUM_DAYS):
        self.params["daily"] = "wind_speed_10m_max"
        self.params["forecast_days"] = num_days
        return self.get_forecast(self.params)

    def get_max_wind_speed(self, num_days=DEFAULT_NUM_DAYS):
        wind_forecast = self.get_wind_forecast(num_days)
        max_wind_speed = max(wind_forecast["daily"]["wind_speed_10m_max"])

        #get day index with max wind speed
        max_wind_day = wind_forecast["daily"]["wind_speed_10m_max"].index(max_wind_speed)
        print(f"La mayor velocidad del viento será de {max_wind_speed} km/h y ocurrirá en {max_wind_day} días")

WeatherForecastClient().get_max_wind_speed(10)
WeatherForecastClient(100,0).get_max_wind_speed(10)
WeatherForecastClient(0,200).get_max_wind_speed(10)
WeatherForecastClient(0,"pepe").get_max_wind_speed(10)
WeatherForecastClient(0,0).get_max_wind_speed(10)
WeatherForecastClient(10.0,10.0).get_max_wind_speed(10)
