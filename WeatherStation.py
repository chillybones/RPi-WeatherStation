from Weather.OpenWeather import OpenWeatherMap, WeatherJSONParser
import requests
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
from DHTReader.DHT_Read import DHT_Read

# Create weather objects
weather = OpenWeatherMap("0f91d7c44a3055005b85971dd63efeef")
parse = WeatherJSONParser()

# Create the DHT object and pass the Pi Pin it is in.
dhtSensor = DHT_Read(21)

# Create the LCD object. Pin numbers can be adjusted to fit any GPIO configuration
GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[8, 10, 11, 12],
              numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

# Allow initialize
sleep(1)

# Do some screen maintainence and wait for the command to execute
lcd.clear()
sleep(5)

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
        indoorReading = dhtSensor.GetReading()

        # Only need one time stamp between both pulls becuase the 5-day and the current will be updated at the same
        # time when needed.
        lastUpdate = datetime.now().time().strftime('%I:%M %p')

        print(currentWeather)
        print("Last update at: %s" % lastUpdate)

        temp = currentWeather.get('CurrentTemp')

        lcd.cursor_pos = (0, 0)
        lcd.write_string(str("Current: %s" % (temp)))
        sleep(1)
        lcd.cursor_pos = (1, 0)
        lcd.write_string(str("%s" % (lastUpdate)))

        # Sleep and incriment counter
        counter =+ currentTimer
        sleep(currentTimer)
