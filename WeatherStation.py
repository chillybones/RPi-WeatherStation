from Weather.OpenWeather import OpenWeatherMap, WeatherJSONParser
import requests
from time import sleep
import datetime
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

# Create weather objects
weather = OpenWeatherMap("0f91d7c44a3055005b85971dd63efeef")
parse = WeatherJSONParser()

# Create the LCD object. Pin numbers can be adjusted to fit any GPIO configuration
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[8, 10, 11, 12],
              numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

# Do some screen maintainence
lcd.clear()
sleep(1)
lcd.home()

# Determine read times - this project will be based off of 30m current weather/6h 10 day forecast updates
# 60 seconds * 30 minutes
currentTimer = 60*30

# (60 sec * 30 min) * 12 half hour segments to get 6 hours worth of segments
tenDayTimer = currentTimer*12

# Seconds counter
counter = 0

# Main loop
while True:
    tenDayForecast = parse.FiveDayParse(weather.GetFiveDayByZip_Imperial("80233"))

    # Loop through the current weather forecase until it is time for 5 day update
    while counter < tenDayTimer:
        currentWeather = parse.CurrentParse(weather.GetWeatherByZip_Imperial("80233"))
        lastUpdate = datetime.datetime

        print(currentWeather)
        print("Last update at: %s" % lastUpdate)

        # Sleep and incriment counter
        counter =+ currentTimer
        sleep(currentTimer)