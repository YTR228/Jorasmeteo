import time
from arduino import read_arduino
from weather_web import get_weather_web
from analyzer import combine_data
from storage import save_data, init_db

INTERVAL = 300  # 5 минут

def run_collector():
    init_db()
    print("Автосбор запущен")

    while True:
        local = read_arduino()
        web = get_weather_web()

        if local or web:
            avg = combine_data(local, web)
            if avg:
                save_data(*avg)
                print("OK:", avg)

        time.sleep(INTERVAL)
