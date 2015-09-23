import smbus

ADDR = 0x10

bus = smbus.SMBus(1)
__debug = False

SWIPE_RIGHT = 0x01
SWIPE_LEFT  = 0x02
SWIPE_UP    = 0x03
HOVER       = 0x05
HOVER_LEFT  = 0x06
HOVER_RIGHT = 0x07
HOVER_UP    = 0x08

def gesture_name(gesture):
    if gesture ==  None or gesture > HOVER_UP:
        return None
    return [
        None,
        'Swipe Right',
        'Swipe Left',
        'Swipe Up',
        None,
        'Hover',
        'Hover Left',
        'Hover Right',
        'Hover Up'
    ][gesture]

def gesture_available():
    status = bus.read_byte_data(ADDR, 0x00)
    if __debug: print("Status: {:08b}".format(status))
    return (status & 0b00011100) > 0

def position_available():
    status = bus.read_byte_data(ADDR, 0x00)
    return (status & 0b00000001) > 0

def get_x():
    return bus.read_byte_data(ADDR, 0x08)

def get_z():
    return bus.read_byte_data(ADDR, 0x0a)

def get_gesture():
    gesture =  bus.read_byte_data(ADDR, 0x04)
    if gesture in [HOVER, HOVER_LEFT, HOVER_RIGHT, HOVER_UP, SWIPE_LEFT, SWIPE_RIGHT, SWIPE_UP]:
        return gesture
    return None

def get_speed():
    return bus.read_byte_data(ADDR, 0x05)
