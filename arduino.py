import serial

SERIAL_PORT = "COM8"
BAUDRATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=2)

def read_arduino():
    line = ser.readline().decode("utf-8").strip()

    try:
        t, h, p = line.split(";")
        return float(t), float(h), float(p)
    except:
        return None
