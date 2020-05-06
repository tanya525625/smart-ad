import requests
import os


class WeatherPrediction:
    def __init__(self, emotion):

        self.city_name = "Saint Petersburg"
        self.city_id = 1496990
        self.appid = "dd7e499466fda051ee3522182ef55d14"
        self.temperature = ["Clear", "Clouds", "Rain", "Snow", "Thunderstorm", "Drizzle"]
        self.emotion = emotion
        self.mod = 3

    def adv_launch(self):
        """Погода на один день"""
        if self.mod == 1:
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                data = res.json()
                print("conditions:", data['weather'][0]['main'])
                print("temp:", data['main']['temp'])
                print("temp_min:", data['main']['temp_min'])
                print("temp_max:", data['main']['temp_max'])
            except Exception as e:
                print("Exception (weather):", e)
            pass

        """Погода на пять дней"""
        if self.mod == 2:
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                                params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                data = res.json()
                for i in data['list']:
                    print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['main'] )
            except Exception as e:
                print("Exception (forecast):", e)
                pass

        """Основная программа - воспроизведение видео"""
        if self.mod == 3:
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params={'id': self.city_id, 'units': 'metric', 'lang': 'ru', 'APPID': self.appid})
                data = res.json()
                weatherGot = data['weather'][0]['main']
                # weatherGot = 'Snow'
                weatherNb = self.temperature.index(weatherGot)
                path = os.path.join(os.path.dirname(__file__), '..', 'videos', weatherGot, weatherGot + '-'
                                    + self.emotion + '.mp4')
                os.startfile(path)
            except Exception as e:
                print("Exception (video):", e)
                pass
