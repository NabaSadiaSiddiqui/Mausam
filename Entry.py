#!/usr/bin/python

try:
	import Tkinter
	from PIL import Image, ImageTk
	from datetime import datetime
	import time
	from WeatherData import WeatherData
except:
	raise ImportError, "Check the following Python modules are available on your system: Tkinter, Image, ImageTk, datetime, time"


class MausamApp(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.initVariables()
		self.setLayout()
		self.setGridOne()
		self.setGridTwoLeft()
		self.setGridTwoRight()
		self.setGridBottom()
		self.update()

	def initVariables(self):
		self.temp = Tkinter.StringVar()
		self.tempDesc = Tkinter.StringVar()
		self.windSpeed = Tkinter.StringVar()
		self.humidity = Tkinter.StringVar()
		self.precipitation = Tkinter.StringVar()
		self.pressure = Tkinter.StringVar()
		self.visibility = Tkinter.StringVar()
		self.setWeather()
		self.monthToStr = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"June", 7:"July", 8:"Aug", 9:"Sept", 10:"Oct", 11:"Nov", 12:"Dec"}

	def setWeather(self):
		data = WeatherData()
		self.temp.set(data.temp)
		self.tempDesc.set(data.tempDesc)
		self.imgLoc = data.icon
		self.windSpeed.set(data.wind)
		self.humidity.set(data.humidity)
		self.precipitation.set(data.precipitation)
		self.pressure.set(data.pressure)
		self.visibility.set(data.visibility)

	def setLayout(self):
		x_out = self.winfo_screenwidth()
		y_out = self.winfo_screenheight()
		self.y_in = y_out*0.8	
		x_in_left = x_out*0.15
		self.x_in_right = x_out*0.85
		
		self.frameOut = Tkinter.Frame(self, width=x_out, height=y_out, bg="FireBrick")
		self.frameOut.pack()
		self.frameIn = Tkinter.Frame(self.frameOut, width=x_out, height=self.y_in, bg="white")
		self.frameIn.place(anchor=Tkinter.CENTER, relx=0.5, rely=0.5)
		
		titleFrame = Tkinter.Frame(self.frameIn, bg="black", height=self.y_in, width=x_in_left)
		titleFrame.place(anchor="w", rely=0.5)
		title = Tkinter.Label(titleFrame, text="MAUSAM", fg="Lime", bg="black", font=("Helvetica", 60, "bold italic"), wraplength=30)
		title.place(anchor="center", relx=0.5, rely=0.5)
		self.panel = Tkinter.Frame(self.frameIn, bg="white", height=self.y_in, width=self.x_in_right)
		self.panel.place(anchor="e", rely=0.5, relx=1)

	"""
	Sets widgets to display 
	- weather description
	- weather icon
	- temperature
	"""
	def setGridOne(self):
		x = self.x_in_right/3
		y = self.y_in
		y_desc = int(y/4)
		y_icon = int(3*y/8)
		self.gridOne = Tkinter.Frame(self.panel, bg="white", height=y, width=x)
		self.gridOne.place(anchor="nw")


		tempFrame = Tkinter.Frame(self.gridOne, bg="white", height=y_icon, width=x)
		tempFrame.place(anchor="nw")
		tempLabel = Tkinter.Label(tempFrame, textvariable=self.temp, bg="white", fg="black", font=("Times", 150))
		tempLabel.place(anchor="w", relx=0.05, rely=0.5)
		scaleLabel = Tkinter.Label(tempFrame, text=u'\u2103', bg="white", fg="black", font=("Times", 50))
		scaleLabel.place(anchor="center", relx=0.8, rely=0.5)

		tempDescFrame = Tkinter.Frame(self.gridOne, bg="white", height=y_desc, width=x, padx=1, pady=1)
		tempDescFrame.place(anchor="w", rely=0.5)
		tempDescLabel = Tkinter.Label(tempDescFrame, textvariable=self.tempDesc, bg="white", fg="black", relief="raised", wraplength=int(x)-5, font=("Times", 35, "italic"))
		tempDescLabel.place(anchor="center", relx=0.5, rely=0.5)

		photo = ImageTk.PhotoImage(Image.open(self.imgLoc))
		tempIconFrame = Tkinter.Frame(self.gridOne, bg="white", height=y_icon, width=x)
		tempIconFrame.place(anchor="w", rely=0.8)
		tempIconLabelFence = Tkinter.Frame(tempIconFrame, bg="black", height=photo.height()+20, width=photo.width()+20)
		tempIconLabelFence.place(anchor="center", relx=0.5, rely=0.5)
		tempIconLabelBorder = Tkinter.Frame(tempIconLabelFence, bg="grey", height=photo.height()+10, width=photo.width()+10)
		tempIconLabelBorder.place(anchor="center", relx=0.5, rely=0.5)
		tempIconLabel = Tkinter.Label(tempIconLabelBorder, image=photo)
		tempIconLabel.image = photo	# work around for a bug in Python Imaging Library that does not properly increment reference count for the object and, so, causes it to be garbage collected --> rendering a grey box instead of the image
		tempIconLabel.place(anchor="center", relx=0.5, rely=0.5)

	"""
	Sets widgets to display 
	- wind
	- humidity
	- pressure
	- precipitation
	- visiblity
	These widgets are positioned on the left half of the top grid
	"""
	def setGridTwoLeft(self):
		x = 2*self.x_in_right/3
		y = self.y_in/2
		self.gridTwo = Tkinter.Frame(self.panel, bg="white", height=y, width=x)
		self.gridTwo.place(anchor="ne", relx=1)

		tempDetailsFrame = Tkinter.Frame(self.gridTwo, bg="white", height=y, width=x/2, padx=75, pady=50)
		tempDetailsFrame.place(anchor="w", rely=0.5)

		windSpeedLabel = Tkinter.Label(tempDetailsFrame, text="Wind:", fg="black", font=("Arial", 15, "bold underline"))
		windSpeedLabel.place(anchor="nw")
		windSpeedVal = Tkinter.Label(tempDetailsFrame, textvariable=self.windSpeed, fg="black", bg="white", font=("Arial", 15, "italic"))
		windSpeedVal.place(anchor="nw", relx=0.6)

		humidityLabel = Tkinter.Label(tempDetailsFrame, text="Humidity:", fg="black", font=("Arial", 15, "bold underline"))
		humidityLabel.place(anchor="nw", rely=0.25)
		humidityVal = Tkinter.Label(tempDetailsFrame, textvariable=self.humidity, fg="black", bg="white", font=("Arial", 15, "italic"))
		humidityVal.place(anchor="nw", relx=0.6, rely=0.25)

		precipitationLabel = Tkinter.Label(tempDetailsFrame, text="Precipitation:", fg="black", font=("Arial", 15, "bold underline"))
		precipitationLabel.place(anchor="nw", rely=0.5)
		precipitationVal = Tkinter.Label(tempDetailsFrame, textvariable=self.precipitation, fg="black", bg="white", font=("Arial", 15, "italic"))
		precipitationVal.place(anchor="nw", relx=0.6, rely=0.5)

		pressureLabel = Tkinter.Label(tempDetailsFrame, text="Pressure:", fg="black", font=("Arial", 15, "bold underline"))
		pressureLabel.place(anchor="nw", rely=0.75)
		pressureVal = Tkinter.Label(tempDetailsFrame, textvariable=self.pressure, fg="black", bg="white", font=("Arial", 15, "italic"))
		pressureVal.place(anchor="nw", relx=0.6, rely=0.75)

		visibilityLabel = Tkinter.Label(tempDetailsFrame, text="Visibility:", fg="black", font=("Arial", 15, "bold underline"))
		visibilityLabel.place(anchor="nw", rely=1)
		visibilityVal = Tkinter.Label(tempDetailsFrame, textvariable=self.visibility, fg="black", bg="white", font=("Arial", 15, "italic"))
		visibilityVal.place(anchor="nw", relx=0.6, rely=1)

	"""
	Sets widgets to display 
	- current date
	- current time
	- observation time
	These widgets are positioned on the right half of the top grid
	"""
	def setGridTwoRight(self):
		x = 2*self.x_in_right/3
		y = self.y_in/2
		self.dateTimeFrame = Tkinter.Frame(self.gridTwo, bg="RosyBrown", height=y, width=x/2)
		self.dateTimeFrame.place(anchor="n", relx=0.71)
		dateTimeFrameInner = Tkinter.Frame(self.dateTimeFrame, bg="white", height=y-30, width=(x/2)-30)
		dateTimeFrameInner.place(anchor="center", rely=0.5, relx=0.5)	
		self.setTime()
		self.setDate()

	"""
	Converts a date object to a string representation --> 2014-07-27 returns July 27
	Sets it on the GUI
	"""
	def setDate(self):
		date = datetime.today().date()
		dateStr = Tkinter.StringVar()
		dateStr.set(self.monthToStr[date.month] + " " + str(date.day))
		dateLabel = Tkinter.Label(self.dateTimeFrame, textvariable=dateStr, fg="black", bg="white", font=("Arial", 25, "bold"))
		dateLabel.place(anchor="center", relx=0.5, rely=0.7)

	"""
	Formats time from AB:CD:EF to XX:XX AM/PM
	Sets it on the GUI
	"""
	def setTime(self):
		time = datetime.today().time()
		timeStr = Tkinter.StringVar()
		timeStr.set(time.strftime("%I:%M %p"))
		timeLabel = Tkinter.Label(self.dateTimeFrame, textvariable=timeStr, fg="black", bg="white", font=("Arial", 50, "bold"))
		timeLabel.place(anchor="center", relx=0.5, rely=0.4)

	"""
	Print meta-information about the application
	on the screen
	"""
	def setGridBottom(self):
		x = 2*self.x_in_right/3
		y = self.y_in/2
		self.gridThree = Tkinter.Frame(self.panel, bg="white", height=y, width=x)
		self.gridThree.place(anchor="se", relx=1, rely=1)
		
		message = Tkinter.Message(self.gridThree, text="ABOUT\nMausam is a desktop weather application which displays basic current weather data of Toronto, Canada. While it can be modified to allow users to select the geographic location, among other options, the beauty of the application is its simplicity. It eliminates the need to open your web browser, navigate to a weather web site and choose your city. Or, find your smartphone and open the weather app/widget. You can hook an old monitor to a Raspberry Pi and have a 24/7 weather service in your room!\n\nThe data hosted by this application is gathered from \"World Weather Online\".\nThis application is written by Naba Sadia Siddiqui (http://github.com/NabaSadiaSiddiqui) using Python's Tkinter module", fg="orange", bg="white", width=x-100, font=("Times", 12, "italic"))
		message.place(anchor="w", rely=0.5)

	"""
	Add callback methods to update the time every 1 minute, date every 1 day and temperature data every 1 hour
	1 min == 60000 ms
	1 hour == 3600000 ms
	1 day == 86400000
	"""
	def update(self):
		ms_min = 60000
		ms_hour = 3600000
		ms_day = 86400000
		self.after(ms_min, self.setTime)
		self.after(ms_hour, self.setWeather)
		self.after(ms_day, self.setDate)

if __name__ == "__main__":
	app = MausamApp(None)
	app.title("Mausam - your local weather app")
	app.mainloop()	# event-driven indefinite looping 
