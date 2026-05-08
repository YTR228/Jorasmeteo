import requests
#set local coords
LAT = 0
LON = 0
#upload your own api
URL = (
)

def get_weather_web():
    try:
        r = requests.get(URL.format(lat=LAT, lon=LON), timeout=10)
        data = r.json()

        temp = data["current_weather"]["temperature"]
        pressure = data["hourly"]["pressure_msl"][0] * 0.75006  # гПа → мм рт.ст
        humidity = data["hourly"]["relative_humidity_2m"][0]

        return round(temp,2), round(humidity,2), round(pressure,2)
    except:
        return None
