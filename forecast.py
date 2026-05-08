import numpy as np
from storage import load_last


def forecast_temperature(hours=3):
    """
    Прогноз температуры на ближайшие часы (линейный тренд)
    """

    data = load_last(60)  # последние 60 измерений

    if len(data) < 10:
        return "⚠ Недостаточно данных для прогноза."

    temps = [row[1] for row in data]

    # вместо времени используем номера измерений
    x = list(range(len(temps)))

    # линейная аппроксимация
    a, b = np.polyfit(x, temps, 1)

    steps = int(hours * 12)

    future_x = x[-1] + steps
    future_temp = a * future_x + b

    now = temps[-1]
    delta = future_temp - now

    text = (
        "🔮 Прогноз температуры\n\n"
        f"Сейчас: {round(now, 2)} °C\n"
        f"Через {hours} ч: {round(future_temp, 2)} °C\n"
        f"Изменение: {round(delta, 2)} °C\n\n"
        "Метод: линейная аппроксимация по локальным данным."
    )

    return text
