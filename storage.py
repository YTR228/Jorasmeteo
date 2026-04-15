import sqlite3
from datetime import datetime

DB = "meteo.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS meteo (
            time INTEGER,
            temperature REAL,
            humidity REAL,
            pressure REAL
        )
    """)
    conn.commit()
    conn.close()


from datetime import datetime

def save_data(temp, hum, press):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    time_str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    cur.execute(
        "INSERT INTO meteo VALUES (?, ?, ?, ?)",
        (time_str, round(temp, 2), round(hum, 2), round(press, 2))
    )

    conn.commit()
    conn.close()



def load_last(n=60):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM meteo ORDER BY time DESC LIMIT ?", (n,))
    rows = cur.fetchall()
    conn.close()
    return rows[::-1]


#экспорт в ксв файлы для чтения эксель
import csv

def export_to_csv(filename="meteo_export.csv"):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT * FROM meteo ORDER BY time")
    rows = cur.fetchall()
    conn.close()

    with open(filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Дата и время", "Температура (°C)", "Влажность (%)", "Давление (гПа)"])
        writer.writerows(rows)

    return filename


