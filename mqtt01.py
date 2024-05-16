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

def rgbmqtt() :
    num = int(input("RANGE FOR LOOP : "))  # จำนวนรอบที่ต้องการวงลูป
    client = mqtt.Client()
    client.connect(host)
    client.publish("dsimju/rgb","RANGE FOR LOOP : "+str(num))

    for x in range(num):
        color = int(input("1.RED 2.GREEN 3.BLUE 4.PINK 5.YELLOW 6.LIGHT_BLUE 7.WHITE 8.OFF 9.EXIT: "))  # สีที่ต้องการแสดง
                
        if color == int(1):
            client = mqtt.Client()
            client.connect(host) #
            client.publish("dsimju/rgb","LED is RED") # แสดงข้อความไปยัง MQTT Topic dsimju/rgb
            print("LED is RED\n")
            GPIO.output(r, 0)  # Turn LED ON
            GPIO.output(g, 1)
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second
        elif color == int(2):
            client = mqtt.Client()
            client.connect(host)
            client.publish("dsimju/rgb","LED is GREEN")
            print("LED is GREEN\n")
            GPIO.output(r, 1)
            GPIO.output(g, 0)  # Turn LED ON
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second
        elif color == int(3):
            client = mqtt.Client()
            client.connect(host)
            client.publish("dsimju/rgb","LED is BLUE")
            print("LED is BLUE\n")
            GPIO.output(r, 1)
            GPIO.output(g, 1)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(4):
            client = mqtt.Client()
            client.connect(host)
            client.publish("dsimju/rgb","LED is PINK")
            print("LED is PINK\n")
            GPIO.output(r, 0)
            GPIO.output(g, 1)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(5):
            client = mqtt.Client()
            client.connect(host)
            client.publish("dsimju/rgb","LED is YELLOW")
            print("LED is YELLOW\n")
            GPIO.output(r, 0)
            GPIO.output(g, 0)
            GPIO.output(b, 1)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(6):
            client = mqtt.Client()
            client.connect(host)
            client.publish("dsimju/rgb","LED is LIGHT BLUE")
            print("LED is LIGHT BLUE\n")
            GPIO.output(r, 1)
            GPIO.output(g, 0)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(7):
            client = mqtt.Client()
            client.connect(host)
            client.publish("dsimju/rgb","LED is WHITE")
            print("LED is WHITE\n")
            GPIO.output(r, 0)
            GPIO.output(g, 0)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(8):
            client = mqtt.Client()
            client.connect(host)
            client.publish("dsimju/rgb","LED is OFF")
            print("LED is OFF\n")
            GPIO.output(r, 1)  # Turn LED OFF
            GPIO.output(g, 1)
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second
        elif color == int(9):
            client = mqtt.Client()
            client.connect(host)
            client.publish("dsimju/rgb","EXITTING PROGRAM")
            print("EXITTING PROGRAM\n")
            break
        else:
            print("ERROR: Invalid color\n")

try:
    rgbmqtt()
    
except KeyboardInterrupt:
    print("\nExiting program.")
GPIO.cleanup()


    
