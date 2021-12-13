from UUGear import *
print "i expect to come here"
device = UUGearDevice('UUGear-Arduino-4465-6200')
print "no way"

# motoru kapatmak için
device.setPinModeAsOutput(3)
device.setPinLow(3)

# motoru açmak için
"""
if device.isValid():
    print "Cihaz var."
    device.setPinModeAsOutput(3)
    for i in range(5):
        device.setPinHigh(3)
        sleep(0.2)
        device.setPinLow(3)
        sleep(0.2)
    device.detach()
    print "cihaz sonlandiriliyor"
    device.stopDaemon()
else:
    print 'UUGear device is not correctly initialize'
"""
