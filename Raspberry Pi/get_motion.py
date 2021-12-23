import RPi.GPIO as IO
import time
from threading import Thread
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(18,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(17,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(27,IO.IN) #GPIO 14 -> IR sensor as input

class GetMotion(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = False
        self.motion_status = False
        IO.output(17,False)
        IO.output(18,False)
    def run(self):
        while True:
            time.sleep(0.3)
            if(self.running==True):
                try :
                    if(IO.input(27)==True): #object is far away
                        IO.output(18,True) #Red led ON
                        # print("someone seen")
                        IO.output(17,False) # Green led OFF
                        self.motion_status=True
                        self.running=False
                    if(IO.input(27)==False): #object is near
                        IO.output(17,True) #Green led ON
                        # print("nobody exist")
                        IO.output(18,False) # Red led OFF
                except KeyboardInterrupt:
                    print("Exiting Ir Led")
                    forever_call = False
                    IO.output(17,False)
                    IO.output(18,False)
                    
    def set_running_status(self):
        IO.output(17,True)
        self.motion_status = False
        self.running = True
    def get_motion_status(self):
        return self.motion_status
    def stop_running(self):
        IO.output(17,False)
        IO.output(18,False)
        self.running = False

