import requests
import os

s_city = "Saint Petersburg"
city_id = 1496990
appid = "dd7e499466fda051ee3522182ef55d14"
temperature = ["Clear", "Clouds", "Rain", "Snow", "Thunderstorm", "Drizzle"]
emotions = ["happiness", "disgust", "surprise"]

mod = 3

# Погода на один день
if mod == 1:
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

# Погода на пять дней
if mod == 2:
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        for i in data['list']:
            print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['main'] )
    except Exception as e:
        print("Exception (forecast):", e)
        pass

# Основная программа - воспроизведение видео
if mod == 3:
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        # emGot = get_emotion()
        emGot = 'disgust'
        weatherGot = data['weather'][0]['main']
        #weatherGot = 'Snow'
        weatherNb = temperature.index(weatherGot)
        path = os.path.join(os.path.dirname(__file__), '..', 'videos', weatherGot, weatherGot + '-'
                            + emGot + '.mp4')
        os.startfile(path)
    except Exception as e:
        print("Exception (adv):", e)
        pass
