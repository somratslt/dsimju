import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
relay_pin = 17  # GPIO pin connected to the relay

GPIO.setup(relay_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(relay_pin, GPIO.HIGH)  # Turn the relay ON
        time.sleep(1)
        GPIO.output(relay_pin, GPIO.LOW)  # Turn the relay OFF
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()