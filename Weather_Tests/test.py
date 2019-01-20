from OpenWeather import OpenWeatherMap, WeatherJSONParser
from time import sleep

weather = OpenWeatherMap("0f91d7c44a3055005b85971dd63efeef")
parse = WeatherJSONParser()

while(True):
    # Time before reading the 5 day forecast again
    totalSeconds = 0

    # Read the 5 day forecast
    fJSON = weather.GetFiveDayByZip_Imperial("80233")
    parse.FiveDayParse(fJSON)

    while(totalSeconds < 3600):
        wJSON = weather.GetWeatherByZip_Imperial("80233")
        currentWeather = parse.CurrentParse(wJSON)

        print(currentWeather)

        # Sleep for 10 seconds before running again
        totalSeconds =+ 60
        sleep(60)