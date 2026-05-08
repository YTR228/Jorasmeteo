import telebot
from storage import export_to_csv
from telebot import types
from analyzer import get_current, pressure_trend
from forecast import forecast_temperature
from config import BOT_TOKEN
from telebot import types

def main_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add("🌡 Погода")
    kb.add("📈 Тренд давления")
    kb.add("🔮 Прогноз")

    return kb


bot = telebot.TeleBot(BOT_TOKEN)

def kb():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True)
    k.row("🌡 Погода","📈 Тренд")
    k.row("🔮 Прогноз")
    return k


@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id,
        "🌍 Интеллектуальная метеостанция\n"
        "Данные собираются автоматически.",
        reply_markup=kb())


@bot.message_handler(func=lambda m: m.text=="🌡 Погода")
def w(m):
    d = get_current()
    if not d:
        bot.send_message(m.chat.id,"Нет данных",reply_markup=kb()); return

    _,t,h,p = d
    bot.send_message(m.chat.id,
        f"🌡Температура: {t} °C\n💧Влажность: {h} %\n⏲Давление: {p} мм рт.ст",
        reply_markup=kb())


@bot.message_handler(func=lambda m: m.text=="📈 Тренд")
def tr(m):
    bot.send_message(m.chat.id,pressure_trend(),reply_markup=kb())


@bot.message_handler(func=lambda m: m.text=="🔮 Прогноз")
def fc(msg):
    text = forecast_temperature()
    bot.send_message(msg.chat.id, text, reply_markup=main_keyboard())


ADMIN_ID = '' #добавить свой собственный айди

@bot.message_handler(commands=['csvqwerty'])
def send_csv_secret(msg):
    if msg.chat.id != ADMIN_ID:
        bot.send_message(msg.chat.id, "⛔ Команда недоступна.")
        return

    file = export_to_csv()
    with open(file, "rb") as f:
        bot.send_document(msg.chat.id, f)

    bot.send_message(msg.chat.id, "✅ Служебный экспорт данных выполнен.")


def run_bot():
    bot.polling(none_stop=True)
