import serial
import serial.tools.list_ports
import struct

good_cereal = None
#Prenegotiated start byte that computer looks for
start_byte = '@'

cereal = None

# collect X Y and Z data, and initialize serial if it hasn't already
def update():
    if cereal == None:
        cereal = instantiateSerial
    data = ('f', [0.0, 0.0, 0.0])
    data = collect()
    return data
 
#open and begin serial
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

#collect data
def collect():
    c = bytes(1)
    if (cereal.in_waiting>0):
        c = cereal.read(1)
        if(c.decode('ascii')=='@'):
            x = cereal.read(4)
            fX = struct.unpack('<f', x)[0]
            y = cereal.read(4)
            fY = struct.unpack('<f', y)[0]
            z = cereal.read(4)
            fZ = struct.unpack('<f', z)[0]
    data = ('f', [fX, fY, fZ])
    return data    

        
    

