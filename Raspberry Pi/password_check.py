import socket
from threading import Thread
import time

class PassChecker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.corect_pass = False
        self.check_pass = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '10.42.0.124'
        self.port = 8888
        self.pass_length_count = 0
        self.password="1234"
        self.input_password=""
        self.socket.connect((self.host,self.port))
        self.charackter='\0'
        self.activated = False
        print("Password handler object ceated")
    def run(self):
        while(True):
            
            tm = self.socket.recv(1)
            charackter =  tm.decode('ascii')
            if(self.check_pass == True and charackter != '\0'):
                self.pass_length_count+=1
                self.input_password+=charackter
                print("charackter", charackter)
                if(self.pass_length_count==4):
                    if(self.input_password == self.password):
                        self.corect_pass = True
                    self.check_pass = False
            elif(charackter=='*'):
                self.activated = True
                    

    def start_pass_check(self):
        self.pass_length_count = 0
        self.input_password=""
        self.corect_pass = False
        self.check_pass = True
    def set_host_and_port(self,host_set,port_set):
        self.port=port_set
        self.host=host_set
    def set_password(self,password_set):
        self.password=password_set
    def get_pass_status(self):
        return self.corect_pass
    def get_activation_status(self):
        return self.activated
    def reset_activation_status(self):
        self.activated=False
    def send_status(self,key):
        self.socket.send(key.encode())
    def get_check_pass(self):
        return self.check_pass
