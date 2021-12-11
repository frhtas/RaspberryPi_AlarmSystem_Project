import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(18,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(17,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(27,IO.IN) #GPIO 14 -> IR sensor as input

forever_call = True
while forever_call:
    
    try :
        if(IO.input(27)==True): #object is far away
            IO.output(18,True) #Red led ON
            print("someone seen")
            IO.output(17,False) # Green led OFF
        
        if(IO.input(27)==False): #object is near
            IO.output(17,True) #Green led ON
            print("nobody exist")
            IO.output(18,False) # Red led OFF
    except KeyboardInterrupt:
        print("Exiting Ir Led")
        forever_call = False
        IO.cleanup()
