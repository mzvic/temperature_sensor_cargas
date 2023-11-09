import adafruit_dht # pip3 install adafruit−circuitpython−dht
import board # pip3 install adafruit−blinka

dht22_in = adafruit_dht.DHT22(board.D14, use_pulseio=False) # DHT22 IN connected to Pin 8 (GPIO14)
dht22_out = adafruit_dht.DHT22(board.D15, use_pulseio=False) # DHT22 OUT connected to Pin 10 (GPIO15)

def get_dht22_in(): # Get temperature and humidity from DHT22 IN

	try :
		return "{}, {} %".format(dht22_in.temperature, dht22_in.humidity) # Return temperature and humidity
	except RuntimeError: # Due to timing issues, sometimes the DHT22 sensor does not respond
		return None, None

def get_dht22_out(): # Get temperature and humidity from DHT22 OUT

	try :
		return "{}, {} %".format(dht22_out.temperature, dht22_out.humidity) # Return temperature and humidity
	except RuntimeError: # Due to timing issues, sometimes the DHT22 sensor does not respond
		return None, None






