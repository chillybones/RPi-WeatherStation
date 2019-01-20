# This is a python library for interacting with the OpenWeatherMap API

# All responses will be returned in JSON format

import requests

class OpenWeatherMap():

    def __init__(self, APIKey):
        """ Provide the API key when constructing the class """
        self.APIKey = APIKey

    def GetAPIKey(self):
       print(self.APIKey)

    def GetWeatherByZip(self, zip):
        self.zip = zip

        url = ("https://api.openweathermap.org/data/2.5/weather?zip=%s&APPID=%s" % (self.zip, self.APIKey))
        response = requests.get(url)

        return response.json()

    def GetWeatherByZip_Imperial(self, zip):
        self.zip = zip

        url = ("https://api.openweathermap.org/data/2.5/weather?zip=%s&units=imperial&APPID=%s" % (self.zip, self.APIKey))
        response = requests.get(url)

        return response.json()

    def GetFiveDayByZip_Imperial(self, zip):
        self.zip = zip

        url = ("https://api.openweathermap.org/data/2.5/forecast?zip=%s&units=imperial&APPID=%s" % (self.zip, self.APIKey))
        response = requests.get(url)

        return response.json()

class WeatherJSONParser():
    def FiveDayParse(self, json):
        self.json = json
        jsonList = json.get("list")
        hiTemp = []
        loTemp = []
        date = []
        # 8 readings a day: 0, 3, 6, 9, 12, 15, 18, 21
        for day in jsonList:
            date.append(day.get("dt_txt"))
            loTemp.append((day.get("main").get("temp_min")))
            hiTemp.append((day.get("main").get("temp_max")))

        # Each set of 8 is one total day
        #for date, hi, lo in zip(date, hiTemp, loTemp):

