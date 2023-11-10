import RPi.GPIO as GPIO

def turn_off_relay():


	GPIO.setmode(GPIO.BCM)

	relay_fan = 21
	relay_extractor = 26

	GPIO.setup(relay_extractor, GPIO.IN)
	GPIO.setup(relay_fan, GPIO.IN)

	GPIO.cleanup()
