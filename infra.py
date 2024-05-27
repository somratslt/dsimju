import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
relay_pin = 11  # GPIO pin connected to the relay
infra_pin = 13

GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setup(infra_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(infra_pin):
            GPIO.output(relay_pin, GPIO.HIGH)  # Turn the relay ON
            time.sleep(0.25)
        else:
            GPIO.output(relay_pin, GPIO.LOW)  # Turn the relay OFF
            time.sleep(0.25)

except KeyboardInterrupt:
    GPIO.cleanup()
