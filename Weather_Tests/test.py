from OpenWeather import OpenWeatherMap, WeatherJSONParser
from time import sleep

weather = OpenWeatherMap("0f91d7c44a3055005b85971dd63efeef")
parse = WeatherJSONParser()

while(True):
    # Time before reading the 5 day forecast again
    totalSeconds = 0

    # Read the 5 day forecast
    forecast = weather.GetFiveDayByZip_Imperial("80202")
    parse.FiveDayParse(forecast)

    while(totalSeconds < 3600):
        response = weather.GetWeatherByZip_Imperial("80202")
        # Sleep for 10 seconds before running again
        totalSeconds =+ 10
        print(response)
        sleep(10)