# Smart Meteo Station
Smart Meteo Station is an educational and research-oriented weather monitoring system based on Arduino Uno, the BMP280 sensor, and Python. The main goal of the project is to improve the accuracy of local meteorological measurements by combining data from a physical home weather station with information obtained from online weather services.

The project was developed as a complete hardware-software complex capable of collecting, storing, analyzing, and forecasting weather data in real time. The system measures air temperature, atmospheric pressure, and humidity using a BMP280 sensor connected to an Arduino Uno microcontroller. The collected data is transmitted to a Python application, where it is processed and stored in a local SQLite database for long-term monitoring and analysis.

To improve measurement reliability, the system integrates data from the Open-Meteo API. Local sensor readings and internet weather data are combined using weighted averaging, allowing the system to reduce the influence of sensor inaccuracies and delays in online weather updates during rapid weather changes.

The project also includes a Telegram bot that provides users with access to current weather conditions, pressure trends, and short-term temperature forecasts. The forecasting system is based on linear approximation of historical measurements and can estimate temperature changes for the next several hours.

Main features of the project include:

Real-time weather monitoring
Automatic data collection and storage
Integration of local and online weather data
SQLite database support
Telegram bot interface
Pressure trend analysis
Short-term temperature forecasting
CSV export for reporting and analysis
Compact long-term data storage

The project uses the following technologies:

Arduino Uno
BMP280 sensor
Python 3
SQLite
NumPy
pySerial
pyTelegramBotAPI
Open-Meteo API

The system architecture consists of several independent modules responsible for sensor communication, internet weather retrieval, data analysis, forecasting, database management, and Telegram bot interaction.

This project demonstrates the possibility of improving local weather monitoring accuracy by combining physical sensor measurements with online meteorological resources. The developed system can be used for educational purposes, scientific experiments, climate observations, and engineering research projects.
