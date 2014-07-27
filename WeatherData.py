#!/usr/bin/python

from urllib2 import Request, urlopen
import json
import urllib
import os

class WeatherData:
	def __init__(self):
		self.initVars()
		self.getData()
		self.getTemp()
		self.getDetails()
	
	def initVars(self):
		cityName = "Toronto"
		respFormat = "json"
		APIKey = "9de1c3ae9b1aefb356b9352bb95b80a86c8d9c10"
		numDays = "1"
		query = "q="+cityName+"&format="+respFormat+"&num_of_days="+numDays+"&key="+APIKey
		self.url = "http://api.worldweatheronline.com/free/v1/weather.ashx?"+query

	def getData(self):
		request = Request(self.url)
		resp = urlopen(request)
		data = json.load(resp)["data"]
		self.weather = data["current_condition"][0]

	def getTemp(self):
		self.temp = self.weather["temp_C"]
		self.tempDesc = self.weather["weatherDesc"][0]["value"]
		self.icon = self.weather["weatherIconUrl"][0]["value"]
		self.downloadImg()

	def downloadImg(self):
		filename = "./res/icon.png"
		if os.path.isfile(filename):
			os.remove(filename)
		urllib.urlretrieve(self.icon, filename)
		self.icon = filename
	
	def getDetails(self):
		self.wind = self.weather["windspeedKmph"] + " km/h"
		self.humidity = self.weather["humidity"] + " %"
		self.precipitation = self.weather["precipMM"] + " mm"
		self.pressure = self.weather["pressure"] + " mb"
		self.visibility = self.weather["visibility"] + " km"


if __name__ == "__main__":
	app = WeatherData()
