import smbus
import time

bus = smbus.SMBus(1)
address = 0x10

def writeNumber(value):
    bus.write_byte(address,value)
    return -1

def readNumber():
    number = bus.read_byte_data(address,1)
    return number

while True:
    var = input("Enter 1-9: ")
    if not var:
    	continue
    writeNumber(var)
    print "RPI: Hi Arduino, I sent you", var
    time.sleep(2)
    number =  readNumber()
    print "Arduino: Hey RPI, I received a digit", number
    print
