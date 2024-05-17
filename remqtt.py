import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

host = "broker.mqtt-dashboard.com"
port = 8884

GPIO.setmode(GPIO.BCM)
relay_pin = 17  # GPIO pin connected to the relay

GPIO.setup(relay_pin, GPIO.OUT)

def on_message(client, userdata,msg):
    pub = msg.payload.decode("utf-8", "strict")
    
    if pub == "on" :
        GPIO.output(relay_pin, GPIO.HIGH)  # Turn the relay ON
        print("ON")
        time.sleep(1)
    elif pub == "off" :
        GPIO.output(relay_pin, GPIO.LOW)  # Turn the relay OFF
        print("OFF")
        time.sleep(1)
    else :
        print("ERROR")


def on_connect(self, userdata, flags, rc):
    print("MQTT Connected.")
    self.subscribe("dsimju/relay") 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()

# try:
#     while True:
#         GPIO.output(relay_pin, GPIO.HIGH)  # Turn the relay ON
#         time.sleep(1)
#         GPIO.output(relay_pin, GPIO.LOW)  # Turn the relay OFF
#         time.sleep(1)

# except KeyboardInterrupt:
#     GPIO.cleanup()