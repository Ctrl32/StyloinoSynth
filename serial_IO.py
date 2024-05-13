import serial
import serial.tools.list_ports

ser = None

def get_comports():
    return serial.tools.list_ports.comports()

def open_comport(port_num:int):
    global ser
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = f"COM{port_num}"
    ser.open()

def is_ready():
    return bool(ser.in_waiting)



def get_reading():
    try:
        packet = ser.readline()
    except:
        return None

    packet = packet.decode("utf-8")
    packet = packet.strip("\n")
    return packet


def get_stylus_data(serial_reading:str, stylus_idx:int):
    data = serial_reading.split("|")

    on_pad = bool(int(data[stylus_idx]))
    pad_idx = int(data[stylus_idx]) - 1

    return on_pad, pad_idx

def set_buzzer(state:bool):
    ser.write(str(int(state)).encode("utf-8"))
