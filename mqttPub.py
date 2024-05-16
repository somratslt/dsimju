import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

host = "broker.mqtt-dashboard.com"
port = 8884

r = 11
g = 13
b = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)    

def on_message(client, userdata,msg):
    pub = msg.payload.decode("utf-8", "strict")

    if pub == "RED" or pub == "red" or pub == "r" :
        print(pub)
        GPIO.output(r, 0)  # Turn LED ON
        GPIO.output(g, 1)
        GPIO.output(b, 1)
        time.sleep(1)  # Wait for 1 second
    elif pub == "GREEN" or pub == "green" or pub == "g" :
        print(pub)
        GPIO.output(r, 1)
        GPIO.output(g, 0)  # Turn LED ON
        GPIO.output(b, 1)
        time.sleep(1)  # Wait for 1 second
    elif pub == "BLUE" or pub == "blue" or pub == "b" :
        print(pub)
        GPIO.output(r, 1)
        GPIO.output(g, 1)
        GPIO.output(b, 0)  # Turn LED ON
        time.sleep(1)  # Wait for 1 second
    elif pub == "OFF" or pub == "off" or pub == "f" :
        print(pub)
        GPIO.output(r, 1)
        GPIO.output(g, 1)
        GPIO.output(b, 1)  # Turn LED OFF
        time.sleep(1)  # Wait for 1 second
    else :
        print("ERROR")
    
 

def on_connect(self, userdata, flags, rc):
    print("MQTT Connected.")
    self.subscribe("dsimju/pub") 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()

GPIO.cleanup()  


