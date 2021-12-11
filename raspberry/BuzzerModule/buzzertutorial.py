#Libraries
import RPi.GPIO as GPIO
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=12 
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
forever_call = True
while forever_call:
    try:
        GPIO.output(buzzer,GPIO.HIGH)
        print ("Beep")
        sleep(0.5) # Delay in seconds
        GPIO.output(buzzer,GPIO.LOW)
        print ("No Beep")
        sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting Buzzer Alarm")
        GPIO.output(buzzer,GPIO.LOW)
        forever_call=False
