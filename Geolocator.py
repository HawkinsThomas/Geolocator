from geolocation.google_maps import GoogleMaps
import datetime,serial


def main():
	print ("hello world")
	currentTime = []
	address = '1280 Main street, Hamilton ON'
	google_maps = GoogleMaps(api_key='AIzaSyAb649ImqHvCeKtAA6YdT3Q6WbRRH2FrrQ')
	location = google_maps.search(location=address)  
	my_location = location.first()
	locationdata = (str(my_location.lat) + ',' + str(my_location.lng))
	timedata = datetime.datetime.now()
	current = str(timedata)
	currentTime. append(current[17:19])
	currentTime. append(current[14:16])
	currentTime. append(current[11:13])
	currentTime. append(current[8:10])
	currentTime. append(current[5:7])
	currentTime. append(current[2:4])
	print(locationdata)
	
	print currentTime[0] + ',' + currentTime[1] + ',' + currentTime[2] + ',' + currentTime[3] + ',' + currentTime[4] + ',' + currentTime[5]


def serialprint(locationdata, timedata):
	#ser = serial.Serial("/dev/tty.usbserial")
	#print ser.name
	ser.write(locationdata)
	ser.write(timedata)
	#ser.close()
	print("")


main() 
