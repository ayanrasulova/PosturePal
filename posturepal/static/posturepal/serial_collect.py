import serial
import serial.tools.list_ports
import struct
import time

# Define serial settings
BAUD_RATE = 115200
START_BYTE = b'@'  # The expected start byte
FLOAT_SIZE = 4  # Each float is 4 bytes
MESSAGE_SIZE = 13  # 1 start byte + 3 floats (4 bytes each)

def find_serial_port():
    """Find and return the first available USB serial port."""
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "USB" in port.description:  # Adjust if necessary for your OS
            return port.device
    return None

def update():
    """Read a 13-byte message from the serial port and return a list of 3 floats."""
    port = find_serial_port()
    
    if not port:
        print("No USB serial device found.")
        return None

    try:
        with serial.Serial(port, BAUD_RATE, timeout=2) as ser:
            while True:
                # Read the first byte and check if it's the start byte
                start = ser.read(1)
                if start == START_BYTE:
                    # Read the next 12 bytes (3 floats)
                    data_bytes = ser.read(12)
                    if len(data_bytes) == 12:
                        # Unpack the bytes into three floats
                        floats = struct.unpack('<fff', data_bytes)
                        return list(floats)  # Convert tuple to list
                
                # If the start byte isn't found, discard and continue reading
                time.sleep(0.01)  # Small delay to avoid CPU overload
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        return None