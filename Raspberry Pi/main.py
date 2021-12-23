from face import FaceRecognition
from password_check import PassChecker
from get_motion import GetMotion
import time

#initialize objects
recognizer_object = FaceRecognition()
password_check= PassChecker()
motion_check = GetMotion()

#start threads
password_check.start()
motion_check.start()
recognizer_object.start()

#start operations
#password_check.start_pass_check()
#recognizer_object.start_recognizer()
password_check.send_status('7')
password_check.send_status('3')
password_check.send_status('5')

def func_beep(time_x,time_y):
    count_xx =time_y
    while(count_xx>0):

        password_check.send_status('6')
        time.sleep(time_x)
        password_check.send_status('7')
        time.sleep(time_x)
        count_xx-=1

def system_start(password,pass_obj):
    pass_obj.set_password(password)
    pass_obj.reset_activation_status()
    while True:
        time.sleep(1)
        if(pass_obj.get_activation_status()==True):
            pass_obj.send_status('1')
            func_beep(0.10,1)
            time.sleep(2)
            break

def pass_check(pass_obj):
    pass_obj.start_pass_check()
    pass_obj.send_status('3')
    pass_obj.send_status('4')
    count=0
    try_count=3
    while True:
        count+=1
        time.sleep(1)
        if(pass_obj.get_pass_status()==True):
            pass_obj.send_status('0')
            time.sleep(2)
            pass_obj.send_status('2')
            pass_obj.send_status('4')
            print("System Active")
            time.sleep(3)
            pass_obj.send_status('3')
            pass_obj.send_status('5')
            func_beep(0.18,4)
            return True
        elif(count==20 or pass_obj.get_check_pass()==False):
            try_count-=1
            if(try_count==0):
                pass_obj.send_status('1')
                time.sleep(1)
                pass_obj.send_status('2')
                pass_obj.send_status('6')
                print("System LOCKED")
                return False
            else:
                count=0
                pass_obj.send_status('6')
                time.sleep(1)
                pass_obj.send_status('7')
                pass_obj.start_pass_check()
                time.sleep(1)



while True:
    print("SYSTEM STARTING")
    password_check.send_status('7')
    password_check.send_status('3')
    password_check.send_status('5')
    system_start("1459",password_check)
    if(pass_check(password_check)==True):
        password_check.reset_activation_status()
        motion_check.set_running_status()
        time_counter = 0
        try_pass=3
        password_check.send_status('4')
        while True:
            time.sleep(1)
            if(password_check.get_activation_status() or motion_check.get_motion_status()):
                password_check.send_status('5')
                password_check.send_status('2')
                if time_counter == 0:
                    print("Started pas check")
                    password_check.start_pass_check()
                    recognizer_object.start_recognizer()
                
                if(password_check.get_pass_status() or recognizer_object.get_recognization_status()):
                    func_beep(0.10,4)
                    break
                if(password_check.get_check_pass()==False and not try_pass==0 ):
                    try_pass-=1
                    if try_pass == 0:
                        print("alarrrm")
                        password_check.send_status('6')
                        while True:
                            try :
                                pass
                            except KeyboardInterrupt:
                                password_check.send_status('7')
                                break
                    else:
                        password_check.send_status('6')
                        time.sleep(1)
                        password_check.send_status('7')
                        print("try again")
                        password_check.start_pass_check()
                if(time_counter==60):
                    password_check.send_status('6')
                    while True:
                        try :
                            pass
                        except KeyboardInterrupt:
                            password_check.send_status('7')
                            break




                time_counter+=1
        recognizer_object.reset_recognizer()
        motion_check.stop_running()
        print("sysytem succesfully closed")

    else:
        while True:
            try :
                pass
            except KeyboardInterrupt:
                password_check.send_status('7')