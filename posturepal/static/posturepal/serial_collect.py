import serial
import serial.tools.list_ports
import struct

good_cereal = None
start_byte = '@'


def update():
    data = ('f', [0.0, 0.0, 0.0])
    instantiateSerial
   

    return data
 

def instantiateSerial():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "USB" in port.description:
            good_cereal = port.device
            break
    if good_cereal:
        try:
            cereal = serial.Serial(good_cereal, 115200)
            print(f"Connected to rf nano on port {good_cereal}")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
    else:
        print("Rf nano not found")

        
    

