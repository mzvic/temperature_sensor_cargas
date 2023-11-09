import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

relay_fan = 21
relay_extractor = 26

def extractor_on():
    GPIO.setup(relay_extractor, GPIO.OUT)

def extractor_off():
    GPIO.setup(relay_extractor, GPIO.IN)

def fan_on():
    GPIO.setup(relay_fan, GPIO.OUT)

def fan_off():
    GPIO.setup(relay_fan, GPIO.IN)


fan_on()
extractor_on()
