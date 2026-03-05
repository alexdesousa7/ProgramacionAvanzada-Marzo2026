import requests

class WeatherForecastClient:
    def __init__(self, latitude = 40, longitude = -2):
        self.base_url = "https://api.open-meteo.com/v1/forecast"
        self.params = {
            "latitude": latitude,
            "longitude": longitude,
            "timezone": "auto"
        }

    def get_forecast(self, params):
        res = requests.get(self.base_url, params=self.params)
        return res.json()


    def get_wind_forecast(self, num_days):
        self.params["daily"] = "wind_speed_10m_max"
        self.params["forecast_days"] = num_days
        return self.get_forecast(self.params)

    def get_max_wind_speed(self, num_days):
        wind_forecast = self.get_wind_forecast(num_days)
        max_wind_speed = max(wind_forecast["daily"]["wind_speed_10m_max"])

        #get day index with max wind speed
        max_wind_day = wind_forecast["daily"]["wind_speed_10m_max"].index(max_wind_speed)
        print(f"La mayor velocidad del viento será de {max_wind_speed} km/h y ocurrirá en {max_wind_day} días")


WeatherForecastClient(0,0).get_max_wind_speed(10)
