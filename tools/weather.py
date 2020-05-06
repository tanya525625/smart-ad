import requests
import os


class AdvLauncher:
    def __init__(self, emotion, city_id):

        self.city_id = city_id
        self.app_id = "dd7e499466fda051ee3522182ef55d14"
        self.weather = ["Clear", "Clouds", "Rain", "Snow", "Thunderstorm", "Drizzle"]
        self.emotion = emotion
        self.mod = "run"  # run or test mode

    def adv_show(self):
        """One day broadcast"""
        if self.mod == "test":
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                   params={'id': self.city_id, 'units': 'metric', 'lang': 'ru', 'APPID': self.app_id})
                data = res.json()
                print("conditions:", data['weather'][0]['main'])
                print("temp:", data['main']['temp'])
                print("temp_min:", data['main']['temp_min'])
                print("temp_max:", data['main']['temp_max'])
            except Exception as e:
                print("Exception (weather):", e)
            pass

        """Main program - video launching"""
        if self.mod == "run":
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                   params={'id': self.city_id, 'units': 'metric', 'lang': 'ru', 'APPID': self.app_id})
                data = res.json()
                weather_got = data['weather'][0]['main']
                path = os.path.join(os.path.dirname(__file__), '..', 'videos', weather_got, weather_got + '-'
                                    + self.emotion + '.mp4')
                os.startfile(path)
            except Exception as e:
                print("Exception (video):", e)
                pass
