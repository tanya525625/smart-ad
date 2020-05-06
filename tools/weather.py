import requests
import os
import subprocess, sys
from cv2 import cv2


class AdvLauncher:
    def __init__(self, emotion, city_id):

        self.city_id = city_id
        self.app_id = "dd7e499466fda051ee3522182ef55d14"
        self.weather = ["Clear", "Clouds", "Rain", "Snow", "Thunderstorm", "Drizzle"]
        self.emotion = emotion
        self.mod = "run"  # run or test mode

    def adv_show(self, frame):
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
                #check if someone standing opposite billboard
                isAnyFace = isAnyFaceThere(frame)
                if (isAnyFace):
                    path = os.path.join(os.path.dirname(__file__), '..', 'videos', weather_got, weather_got + '-'
                                    + self.emotion + '.mp4')
                else:
                    path = os.path.join(os.path.dirname(__file__), '..', 'videos', weather_got, weather_got + '-'
                                    + 'default.mp4')
                
                opener ="open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, path])
            except Exception as e:
                print("Exception (video):", e)
                pass

def isAnyFaceThere(frame):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
        return False
    else:
        return True