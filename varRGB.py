import RPi.GPIO as GPIO
import time

r = 11
g = 13
b = 15

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setwarnings(False)

def conRGB() :
     num = int(input("RANGE FOR LOOP : "))  # จำนวนรอบที่ต้องการวงลูป
     for x in range(num):
        
            print("LED is RED\n")
            GPIO.output(r, 0)  # Turn LED ON
            GPIO.output(g, 1)
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second
        
            print("LED is GREEN\n")
            GPIO.output(r, 1)
            GPIO.output(g, 0)  # Turn LED ON
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second
        
            print("LED is BLUE\n")
            GPIO.output(r, 1)
            GPIO.output(g, 1)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        
            print("LED is PINK\n")
            GPIO.output(r, 0)
            GPIO.output(g, 1)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        
            print("LED is YELLOW\n")
            GPIO.output(r, 0)
            GPIO.output(g, 0)
            GPIO.output(b, 1)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
       
            print("LED is LIGHT BLUE\n")
            GPIO.output(r, 1)
            GPIO.output(g, 0)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
     
            print("LED is WHITE\n")
            GPIO.output(r, 0)
            GPIO.output(g, 0)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
       
            print("LED is OFF\n")
            GPIO.output(r, 1)  # Turn LED OFF
            GPIO.output(g, 1)
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second

def conRGB2():
    num = int(input("RANGE FOR LOOP : "))  # จำนวนรอบที่ต้องการวงลูป
    for x in range(num):
        color = int(
            input("1.RED 2.GREEN 3.BLUE 4.PINK 5.YELLOW 6.LIGHT_BLUE 7.WHITE 8.OFF : ")
        )  # สีที่ต้องการแสดง
        if color == int(1):
            print("LED is RED\n")
            GPIO.output(r, 0)  # Turn LED ON
            GPIO.output(g, 1)
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second
            return "RED"
        elif color == int(2):
            print("LED is GREEN\n")
            GPIO.output(r, 1)
            GPIO.output(g, 0)  # Turn LED ON
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second
        elif color == int(3):
            print("LED is BLUE\n")
            GPIO.output(r, 1)
            GPIO.output(g, 1)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(4):
            print("LED is PINK\n")
            GPIO.output(r, 0)
            GPIO.output(g, 1)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(5):
            print("LED is YELLOW\n")
            GPIO.output(r, 0)
            GPIO.output(g, 0)
            GPIO.output(b, 1)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(6):
            print("LED is LIGHT BLUE\n")
            GPIO.output(r, 1)
            GPIO.output(g, 0)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(7):
            print("LED is WHITE\n")
            GPIO.output(r, 0)
            GPIO.output(g, 0)
            GPIO.output(b, 0)  # Turn LED ON
            time.sleep(1)  # Wait for 1 second
        elif color == int(8):
            print("LED is OFF\n")
            GPIO.output(r, 1)  # Turn LED OFF
            GPIO.output(g, 1)
            GPIO.output(b, 1)
            time.sleep(1)  # Wait for 1 second
        else:
            print("ERROR: Invalid color\n")
        return num

try:
       conRGB()
       numtext = conRGB2() 
       print("NUMTEXT "+str(numtext))  
   

except KeyboardInterrupt:
    print("\nExiting program.")
GPIO.cleanup()

